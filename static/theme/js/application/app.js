var data = [
    {author: "Саня Коровкин", text: "первый отзыв"},
    {author: "Леха Пахомов", text: "второй отзыв"}
];

var ReviewForm = React.createClass({
    render: function(){
        return (
            <div className="reviewForm">
                Hello, Aleks! I am a reviewForm.
            </div>
        );
    }
});


// tutorial7.js
var Review = React.createClass({
  render: function() {
    var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
    return (
      <div className="comment">
        <h2 className="commentAuthor">
          {this.props.author}
        </h2>
        <span dangerouslySetInnerHTML={{__html: rawMarkup}} />
      </div>
    );
  }
});


var ReviewList = React.createClass({
    render: function(){        
        var reviewNodes = this.props.data.map(function (review) {
            return (
                <Review author={review.author}>
                    {review.text}
                </Review>
            );
        });
        return (
            <div className="reviewList">
                {reviewNodes}
            </div>
        );       
    }
});

var ReviewBox = React.createClass({
    render: function () {
        return (
            <div className="reviewBox">
                <h1>Reviews</h1>
                <ReviewList data={this.props.data} />
                <ReviewForm />
            </div>
        );
    }
});

React.render(
    <ReviewBox data={data} />,
    document.getElementById('reviews')
)
