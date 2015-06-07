var React = require('react');

var FlatButton = require('material-ui').FlatButton;
var Dialog = require('material-ui').Dialog;
var TextField = require('material-ui').TextField;
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var injectTapEventPlugin = require("react-tap-event-plugin");

var AnswerList = require('./Answers.jsx');
var AnswerModal = require('./AnswerModal.jsx');
var QuestionModal = require('./QuestionModal.jsx');
var FaqActions = require('../actions/FaqActions.js');


var Question = React.createClass({
	render: function () {		
		return (
			<div className="col-xs-12">
				<div className="question-faq">
					<h2 ref="title_question">{this.props.question.title} <span className="small question-date">{this.props.question.date}</span></h2>
					<p ref="text_question">{this.props.question.text}</p>					
					<AnswerModal id={this.props.question.id} user={this.props.user} />
				</div>
				<div className="answers">					
					<AnswerList answers={this.props.question.answers} />
				</div>
			</div>
		)
	}
});


var QuestionList = React.createClass({
	render: function () {
		var user = this.props.user;
		items = this.props.collection.map(function (item){
			return (
				<Question question={item} user={user}/>
			)
		});
		return (			
			<div className="row">				
				<QuestionModal />
				{items}
			</div>
		)
	}
});


module.exports = QuestionList;