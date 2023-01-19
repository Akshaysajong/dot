
// $(document).ready(function()
// {
// var country = $("#country");
// var state = $("#state");
// var city = $('#city');
// var $options = state.find('option');

// country.on('change',function(){
//         state.html($options.filter('[value="'+ this.value +'"]'));
//     }).trigger('change');
// });

function confdelete(){
    var result = confirm("Are you sure to delete?");
    if(result){
      console.log("Deleted")
    }
    else{
      preventDefault();
    }
    }
  

function  get_country(){
    jQuery.ajax({
        type: 'get',
        url: "/ajax_country/",
        data:{
            'country':$('#country').val()
        },
        dataType: 'json',
        success: function(data)
        {
            var op = '<option value="">--Select--</option>' 
            for(st in data){
                op += '<option value="'+data[st].id+'">'+ data[st].name + '</option>' 
            }
            $('#state').html(op)

        }
    })
}


function get_state()
{

    jQuery.ajax({
        type: 'get',
        url: "/ajax_state/",
        data:{
            'state' : $('#state').val()
        },
        dataType: 'json',
        success: function(data)
        {
            var op = '<option value="">--Select--</option>' 
            for(st in data){
                op += '<option value="'+data[st].id+'">'+ data[st].name + '</option>' 
            }
            $('#city').html(op)

        }
    })

}



// function delete_hotel(){
//     var result = confirm("Are you sure to delete?");
//     if(result){
//       console.log("Deleted")
//     }
//     else{
//       event.preventDefault();
//     }
//   }

  
function delete_hotel(id){
    jQuery.ajax({
        type : 'get',
        url : "/delete_hotel/",
        data : {
            d_id : id
        },
        dataType : 'jason',
        success: function(data)
        {
            alert('Hotel deleted')
            window.location.reload()
            
        }
    })
}


function delete_darea(id){
    jQuery.ajax({
        type : 'get',
        url : "/delete_darea/",
        data : {
            d_id : id
        },
        dataType : 'jason',
        success: function(data)
        {
            alert('Destination area deleted')
            
        }
    })
}