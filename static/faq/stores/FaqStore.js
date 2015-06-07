var FaqDispatcher = require('../dispatcher/FaqDispatcher.js');
var MicroEvent = require('microevent');
var $ = require('jquery');
var snackbar = require('../lib/snackbar.js');
var merge = require('merge');
var Cookies = require('js-cookie');


// - Хранилище которое содержит наше текущее состояние 
// - Когда выполняется какой то метод в Диспетчере, мы меняем это 
// состояние на актуальное
// - Так же из Диспетчера, при изменении данных, вызывается соотвтествующая
// функция AppStora, на которую подписан Умный компонтент, который в итоге
// меняет state
var FaqStore = merge(MicroEvent.prototype, {

    user: {},
    collection: [],

    userChange: function() {
        this.trigger('change');
    },
    collectionChange: function () {
        this.trigger('change');
    }

});


FaqDispatcher.register(function (payload) {

    switch (payload.actionType) {

        case 'get-faqtree-action':
            $.ajax({
                url: '/api/v1/faq-tree/',
                dataType: 'json',
                cache: false,
                success: (function (data) {

                    FaqStore.collection = data;
                    FaqStore.collectionChange();

                }).bind(this),
                error: (function (xhr, status, err) {
                    console.log('error fetchin collection');
                }).bind(this)
            });

        break;

        case 'get-user-action':
            $.ajax({
                url: '/api/v1/user/',
                dataType: 'json',
                cache: false,
                success: (function (data) {

                    FaqStore.user = data;
                    FaqStore.userChange();                    

                }).bind(this),
                error: (function (xhr, status, err) {
                    console.log('error fetchin user');
                }).bind(this)
            });

        break;

        case 'post-answer-action':
            var csrftoken = Cookies.get('csrftoken');
            $.post(
                "/api/v1/post-answer/",
                {
                    csrfmiddlewaretoken: csrftoken,
                    id: payload.answer.id,
                    text: payload.answer.text
                }
            ).success(
                function (data) {
                    $.snackbar({timeout: 5000, content: data.message });                

                    for (var i = 0; i < FaqStore.collection.length; i++){                        
                        if (FaqStore.collection[i].id == data.question_id){                            
                            FaqStore.collection[i].answers.push({
                                photo: data.photo,
                                name: data.name,
                                date: data.date,
                                text: data.text
                            });
                            break
                        }
                    }

                    FaqStore.collectionChange();
                })
            .error(
                function (data) {
                    console.log("Ошибка post запроса при добавлении ответа");
                    $.snackbar({timeout: 5000, content: data.message });
                });

            break;

        case 'post-question-action':
            var csrftoken = Cookies.get('csrftoken');
            $.post(
                "/api/v1/post-question/",
                {
                    csrfmiddlewaretoken: csrftoken,                    
                    text: payload.question.text,
                    title: payload.question.title
                }
            ).success(
                function (data) {
                    $.snackbar({timeout: 5000, content: data.message });

                    FaqStore.collection.unshift({
                        'id': data.question_id,
                        'title': data.title,
                        'text': data.text,
                        'date': data.date,
                        'answers': data.answers
                    });

                    FaqStore.collectionChange();
                })
            .error(
                function (data) {
                    console.log("Ошибка post запроса при добавлении вопроса");
                    $.snackbar({timeout: 5000, content: data.message });
                });

            break;

        default:
    };

    return true;
});


module.exports = FaqStore;
