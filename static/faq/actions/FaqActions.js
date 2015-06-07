var FaqDispatcher = require('../dispatcher/FaqDispatcher.js');
    
    var FaqActions = {
        getFaqTree: function () {
            FaqDispatcher.dispatch({
                actionType: "get-faqtree-action",
            });
        },
        getCurrentUser: function() {
            FaqDispatcher.dispatch({
                actionType: "get-user-action",
            });
        },
        answer: function (answer) {
            FaqDispatcher.dispatch({
                actionType: "post-answer-action",
                answer: answer
            });
        },
        question: function (question) {
            FaqDispatcher.dispatch({
                actionType: "post-question-action",
                question: question                
            });
        }
    }

module.exports = FaqActions;