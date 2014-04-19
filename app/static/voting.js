$(".voting p:nth-child(1)").click(function() {
	//var id = $(this).data("storyid");
	var id = parseInt($(this).parent().attr('storyid'));
	$.post("/vote/" + id, {vote: 'up'}, function success(data) {
			//alert("upvote: " + data);
		})
})

$(".voting p:nth-child(3)").click(function() {
	//var id = $(this).data("storyid")
	var id = parseInt($(this).parent().attr('storyid'));
	$.post(
		"/vote/" + id, 
		{vote: 'down'}, 
		function success(data) {
			//alert("downvote: " + data);
		}, 
		function failure(data) { 
			alert("fail");
		}
	)
})