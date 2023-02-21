

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
    alert(' Are you sure to delete?')  
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

function deleteimgcontent(obj, id){
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

// function delvariation(id) {
//     $('#deleted_variations').val($('#deleted_variations').val() + ', '+id);
// }




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


function createpath(obj) {
    $('#path').val(obj.value.toLowerCase().replace(/ /g,'_').replace(/\//g,''));
    }
      

function addvariation(c, p) {
    rl = $('.'+c).length + 1;
    row = '<div class="row mb-3 border-bottom pb-3 ' + c + '" id="'+ c + rl +'"><input type="hidden" name="variationai[]" value="' + (999 + rl) + '">' + $('#'+c+'1').html().replace('imagevariation1000', 'imagevariation'+(999 + rl)) + '</div>';
    $('#' + p).append(row);
    $('#' + c + rl +' input').val(''); 
    $('#' + c + rl +' .imgwrapper').remove(); 
}

function delparentrow(o, c) {
    if($(o).parent().parent().attr('id') != c+'1') {
      $(o).parent().parent().remove();
    }
  }
  
    

function upload_variationimg(obj, f) {
    var file = obj.files[0];
    var imageholder = $(obj).parent().parent();
    var idnum = $(obj).attr('id').replace('imagevariation', '');
    var reader  = new FileReader();
    v = (f==0)?'':'e';
    f = (f==0)?idnum:f;
    // it's onload event and you forgot (parameters)
    reader.onload = function(e)  {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            imageholder.append('<div class="row mb-3 border-bottom pb-3 imgwrapper"><div class="col-md-4"><img src="' + server +'/'+ this.responseText +'" class="img-responsive" onclick="popprodImage(this, \'' + this.responseText + '\')" style="width:100px;"><input type="hidden" class="form-control" name="' + v +'variationimage[' + f +'][]" value="'+ this.responseText +'"></div><div class="col-md-4"><input type="number" class="form-control" name="' + v +'variationimgweight[' + f +'][]" value="1"></div><div class="col-md-4"><a href="#" onclick="deleteVariationImage(this, \''+ this.responseText +'\')" title="Delete"><span class="bi-trash" style="font-size: 30px; color: black;"></span></a></div></div>');
          }
        };
        xhttp.open("POST", server + "/uploadproductimage", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("photo=" + encodeURIComponent(e.target.result));
     }
     // you have to declare the file loading
     reader.readAsDataURL(file);
  }
  
  

  
  $(document).ready(function() {
    $('#subscribe-form').submit(function(event) {
        event.preventDefault();
        var email = $('#email').val();
        $.ajax({
            url: '/subscription/',
            type: 'POST',
            data: {email: email},
            success: function(response) {
                alert('Thank you for subscribing');
            },
            error: function(xhr, status, error) {
                var message = JSON.parse(xhr.responseText).message;
                alert(message);
            }
        });
    });
});