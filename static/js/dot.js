

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
            alert(data.msg);
            window.location.reload();
            
        }
    })
}

function delete_destination(id){
    jQuery.ajax({
        type : 'get',
        url : "/delete_destination/",
        data : {
            d_id : id
        },
        dataType : 'jason',
        success: function(data)
        {
            alert('Destination deleted')
            window.location.reload()
            
        }
    })

}


function confdelete(obj, id) {
var result = confirm("Are you sure to delete?");
console.log(result.length)
var count= 0
console.log(count)
if(result){

    a=document.getElementById('deletedfiles').value = document.getElementById('deletedfiles').value+', '+id;
    console.log(a)
    obj.parentElement.parentElement.style.display = 'none';
}
}