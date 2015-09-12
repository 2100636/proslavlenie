$('.swiper-wrapper img').click(function (e) {
	var link = $(e.target).attr('link');
	// console.log('swiper-wrapper clicked e.target: ', e.target);
	// console.log('swiper-wrapper clicked attrs: ', link);
	window.location = link;
});