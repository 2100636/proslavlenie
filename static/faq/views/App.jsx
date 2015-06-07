var React = require('react');
var $ = require('jquery');

var QuestionList = require('./Questions.jsx');
var FaqActions = require('../actions/FaqActions.js');
var FaqStore = require('../stores/FaqStore.js');


var App = React.createClass({
	getInitialState: function () {
        return {
            collection: [],
          	user: {}
        }
    },
    
    componentDidMount: function () {       
        FaqActions.getFaqTree();
        FaqActions.getCurrentUser();
        FaqStore.bind( 'change', this.collectionChanged );
        FaqStore.bind( 'change', this.userChanged );          
    },
    componentWillUnmount: function () {
        FaqStore.unbind( 'change', this.collectionChanged );
        FaqStore.unbind( 'change', this.userChanged );
    },
    collectionChanged: function () {
        this.setState({
            collection: FaqStore.collection
        });          
    },
    userChanged: function () {
        this.setState({
            user: FaqStore.user
        });                 
    },
	render: function () {		
		return (
			<QuestionList collection={this.state.collection} user={this.state.user} />
		)
	}
});

module.exports = App;