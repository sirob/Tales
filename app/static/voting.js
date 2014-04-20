$(".voting p:nth-child(1)").click(function() {
	var id = parseInt($(this).parent().attr('storyid'));
	var counter = $(this).parent().children()[1];
	$.post("/vote/" + id, {vote: 'up'}, function success(data) {
			counter.innerText = data;
		})
})

$(".voting p:nth-child(3)").click(function() {
	var id = parseInt($(this).parent().attr('storyid'));
	var counter = $(this).parent().children()[1];
	$.post("/vote/" + id, {vote: 'down'}, function success(data) {
			counter.innerText = data;
		})
})