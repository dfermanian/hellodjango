$(function() {
	$( "#sortable" ).sortable({
		update: function( event, ui ){
			var list = $('#sortable li');
			console.log(list);
			var elts = [];
			$.each(list, function(index, value){
				if($(value).data('id')){
					elts.push({"id": $(value).data('id'), "position": index});
			}
			});
			
			console.log(elts);
			data = {"list": elts}
			$.ajax({
				url: "http://localhost:8000/services/moveitem",
				type: 'POST',
				contentType: "application/json",
				dataType: "text",
				data: JSON.stringify(data),
				success: function(){console.log('success')}
			});
			
		}
	});
	$( "#sortable" ).disableSelection();
	//services/addbucket

	//copy item
	$( ".bucket-child" ).droppable({
		activeClass: "ui-state-hover",
		drop: function( event, ui ) {
			console.log($(this), ui.draggable);
			var data = {"bucket_id": $(this).data('id'), "item_id": $(ui.draggable).data('id')}
			$.ajax({
				url: "http://localhost:8000/services/copyitem",
				type: 'POST',
				contentType: "application/json",
				dataType: "text",
				data: JSON.stringify(data),
				success: function(){console.log('success')}
			});
			
		}
	});
	
	//add top bar bucket
	$('.bucket-outline-add').on('click', function(){
		pos = $('#sortable li');
		console.log(pos);
		var answer = prompt ("New bucket name: ");
		console.log(answer);
		var newBucket = $(document.createElement("div"));
		newBucket.addClass("bucket-child");
		newBucket.html(answer);
		var container = $(document.createElement("div"));
		container.append(newBucket);
		container.addClass("bucket-outline");
		$('#add-bucket').before(container);
		answer prompt 
		var data = {"position": pos, "name": answer}
		$.ajax({
			url: "http://localhost:8000/services/additem",
			type: 'POST',
			contentType: "application/json",
			dataType: "text",
			data: JSON.stringify(data),
			success: function(){console.log('success')}
		});
	});
	
	//add item
	$('.bucket-wrapper-add').on('click', function(){
		console.log('additem');
	});
	
});