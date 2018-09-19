$(document).ready(function() {
				var trigger = $('.hamburger'),
					overlay = $('.overlay'),
					isClosed = true,
					picture = $('#picture')

				trigger.click(function() {
					hamburger_cross();
				});

				function hamburger_cross() {

					if(isClosed == true) {
						overlay.hide();
						trigger.removeClass('is-open');
						trigger.addClass('is-closed');
						isClosed = false;
						setTimeout(function(){picture.css("position","absolute");},300);
						
					} else {
						overlay.show();
						trigger.removeClass('is-closed');
						trigger.addClass('is-open');
						isClosed = true;
						picture.css("position","fixed");
					}
				}

				$('[data-toggle="offcanvas"]').click(function() {
					$('#wrapper').toggleClass('toggled');
				});
			});
			$("body").on('click', '[data-stopPropagation]', function(e) {
				e.stopPropagation();
			});