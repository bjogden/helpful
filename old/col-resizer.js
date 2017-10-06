// handle resizing of projects columns at bryceogden.com/projects
var resized;

$(document).ready(function() {
	initialLargeWidth();
	widthChangeHandler();
});

function initialLargeWidth() {
	if (window.innerWidth >= 992) {
		setTimeout( function() {
			resizeColumns('.projects .col-md-4');
			console.log('initial column resize done');
		}, 250);
	}
}

function widthChangeHandler() {
	var es = $('.projects .col-md-4');
	resized = 0;

	$(window).resize(function() {

		if (window.innerWidth >= 992 && resized != 1) {
			resizeColumns('.projects .col-md-4')
			resized = 1;
			console.log('resized columns for larger');

		} else if (window.innerWidth < 992 && resized != 2) {
			resize(es, 'auto');
			resized = 2;
			console.log('resized columns for smaller');
		}
	});
}

function resizeColumns(selector, use_auto_or_maxHeight_bool) {	
	var ps = $(selector),
		e,
		a = [],
		c = 0,
		r,
		i,
		h = 0,
		t;

	$.each(ps, function(index, element) {
		c++;
		r = c % 3;
		j = parseInt((c-1) / 3);
		e = $(element);
		r == 1 ? a.push([e.height()]) : a[j].push(e.height());

		if ( h < e.height() ) h = e.height();
		if (r == 0) {
			resize(ps.slice(index-2, c), h);
			h = 0;
		}
	});

	//console.log("those found by '"+selector+"' have been resized");
}

function resize(element_array, new_height) {
	for (var i = 0; i < element_array.length; i++) {
		element_array[i].style.height = new_height;
	}
}