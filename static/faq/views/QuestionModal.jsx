var React = require('react');

var FlatButton = require('material-ui').FlatButton;
var Dialog = require('material-ui').Dialog;
var TextField = require('material-ui').TextField;
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var injectTapEventPlugin = require("react-tap-event-plugin");

var FaqActions = require('../actions/FaqActions.js');


var QuestionModal = React.createClass({
	getInitialState: function () {
	    return {
	        modal: true  
	    };
	},
    childContextTypes: {
        muiTheme: React.PropTypes.object
    },
    getChildContext: function() {        
        return {
            muiTheme: ThemeManager.getCurrentTheme()
        };
    },
    _showModal: function () {
    	this.refs.questionDialog.show();
    },    
    _DialogCancel: function () {
    	this.refs.questionDialog.dismiss();
    },
    _DialogSubmit: function (e) {
		e.preventDefault();
        FaqActions.question({        	
            text: this.refs.text_ref.getValue(),
            title: this.refs.title_ref.getValue()
        });
        this.refs.questionDialog.dismiss();
	},
    render: function () {
    	var questionActions = [
			  <FlatButton
			    label="Закрыть"				    
			    secondary={true}
			    className="modal-button-cancel"
			    onClick={this._DialogCancel} />,
			  <FlatButton
			    label="Отправить вопрос"
			    primary={true}
			    className="modal-button-ok"
			    onClick={this._DialogSubmit} />
			];
		var modalForm = [														
			<TextField
				ref="title_ref"
				hintText="Дайте общее название вопросу"
				style={{width: '100%', margin: '0 auto'}}
				floatingLabelText="Введите название вопроса"/>,
		 	<TextField
			  	ref="text_ref"
			  	hintText="Ваш вопрос"
			  	style={{width: '100%', margin: '0 auto'}}
			  	multiLine={true}
			  	floatingLabelText="Введите текст (поле ввода расширяется автоматически)"/>
			];					
		var modalQuestion = [
			<Dialog
              ref="questionDialog"
			  title="Задать вопрос"
			  actions={questionActions}
			  modal={this.state.modal}>
			  {modalForm}
			</Dialog>	
			];
        return (			
            	<div>
            		<button onClick={this._showModal} className="btn btn-primary">Задать вопрос</button>
					{modalQuestion}
				</div>
        )        
    }
});


module.exports = QuestionModal;