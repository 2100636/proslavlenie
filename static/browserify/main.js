var $ = require('jquery');
require('fancybox')($);
 
$(document).ready(function() {
    // $.fancybox.open($('.fancybox-me'));
    $('.fancybox-me').fancybox();
});