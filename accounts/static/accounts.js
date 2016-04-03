/* global $ */

var initialize = function (navigator, user, token, urls) {
	$('#id_login').on('click', function() {
		navigator.id.request();
	});

	navigator.id.watch({
		loggedInUser: user,
		onlogin: function(assertion) {
			var posting = $.post(
				urls.login, 
				{ assertion: assertion, csrfmiddlewaretoken: token }
			)
			posting.done(function() { window.location.reload(); })
			posting.fail(function() { navigator.id.logout(); });
		},
		onlogout: function() {}
	});
};

window.Superlists = {
	Accounts: {
		initialize: initialize
	}
};