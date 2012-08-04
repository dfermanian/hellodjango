$(function() {
	$( ".sortable, .selected_sortable" ).sortable({
		update: function( event, ui ){
			var list = $('.selected_sortable li');
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
			var data = {"bucket_id": $(this).data('id'), "item_id": $(ui.draggable).data('id')};
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
		pos = $(".bucket-parent .bucket-child").length;
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
		var data = {"position": pos, "name": answer};
		$.ajax({
			url: "http://localhost:8000/services/addbucket",
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
	
	$('.bucket-child').on('click', function(){
		console.log($(this));
		
		console.log("FUCKTHIS");
		var self = $(this);
		if(self.hasClass('selected-bucket')){}
		else{
		$('.bucket-child').removeClass('selected-bucket');
		self.addClass('selected-bucket');
		
		var id = self.data('id');
		$('.selected_sortable').addClass('sortable').removeClass("selected_sortable");
		$('.bucket' + id).addClass("selected_sortable")
						.removeClass("sortable");
						
						
						
							
		}
		
	});
	
	
	
});