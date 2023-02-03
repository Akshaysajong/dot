

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
        dataType : 'json',
        success: function(data)
        {
            alert('Hotel deleted')
            window.location.reload()
            
        }
    })
}


function delete_darea(id){
    alert('Are you sure to delete destination area?');
    jQuery.ajax({
        type : 'get',
        url : "/delete_darea/",
        data : {
            d_id : id
        },
        dataType : 'json',
        success: function(data)
        {
            alert(data);
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
        dataType : 'json',
        success: function(data)
        {
            alert('Destination deleted')
        
            
        }
    })

}

function delete_organization(id){
    alert('Organization deleted')  
    jQuery.ajax({
        type : 'get',
        url : "/delete_organization/",
        data : {
            org_id : id
        },
        dataType : 'json',
        success: function(data)
        {
            alert(data.msg)  
            window.location.reload();  
            
        }
    })

}

function deleteorgtn(obj, id){
    var result = confirm("Are you sure to delete?");
    if(result){
        df = document.getElementById('deletedfiles').value;
        dfc  = df.split(", ");
        if(dfc.length < document.getElementById('imgcount').value) {
            document.getElementById('deletedfiles').value = df+', '+id;
            a=document.getElementById('img_id')
            console.log(a)
            obj.parentElement.parentElement.style.display = 'none';
        }
        else {
            alert('Please keep atleaimagest one ');
        }        
    }
}

function confdelete(obj, id) {
    var result = confirm("Are you sure to delete?");
    if(result){
        df = document.getElementById('deletedfiles').value;
        dfc  = df.split(", ");
        if(dfc.length < document.getElementById('imgcount').value) {
            document.getElementById('deletedfiles').value = df+', '+id;
            a=document.getElementById('img_id')
            console.log(a)
            obj.parentElement.parentElement.style.display = 'none';
        }
        else {
            alert('Please keep atleaimagest one ');
        }        
    }
}

function deletefacility(obj, id) {
    var result = confirm("Are you sure to delete?");
    if(result){
        df = document.getElementById('deletedfiles').value;
        dfc  = df.split(", ");
        if(dfc.length < document.getElementById('imgcount').value) {
            document.getElementById('deletedfiles').value = df+', '+id;
            a=document.getElementById('img_id')
            console.log(a)
            obj.parentElement.parentElement.style.display = 'none';
        }
        else {
            alert('Please keep atleaimagest one ');
        }        
    }
    }