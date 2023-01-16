  var server = "http://localhost/izha/public";
  //var server = "";

  $(document).on("scroll", function() {

    if($(document).scrollTop()>200) {
      $("header").removeClass("large").addClass("small");
    } else {
      $("header").removeClass("small").addClass("large");
    }
    
  });

  $('.owl-carousel').owlCarousel({
      loop:true,
      margin:10,
      responsiveClass:true,
    autoplay:true,
    autoplayTimeout:2500,
    autoplayHoverPause:true,
      responsive:{
          0:{
              items:1,
              nav:true
          },
          600:{
              items:3,
              nav:false
          },
          1000:{
              items:4,
              nav:true,
              loop:false
          }
      }
  })

  $(document).ready(function() {
     /* $('[rel=tooltip]').tooltip({
          placement: 'left'
      });
      $(function () {
        function get15dayFromNow() {
              return $('#enddate').val();
              //return new Date(new Date().valueOf() + 15 * 24 * 60 * 60 * 1000);
          }

          $('#clock-c').countdown(get15dayFromNow(), function(event) {
            var $this = $(this).html(event.strftime(''
              + '<span class="fs-1 fw-bold me-1">%D</span> Day%!d'
              + '<span class="fs-1 fw-bold me-1 ms-4">%H</span> Hr'
              + '<span class="fs-1 fw-bold me-1 ms-4">%M</span> Min'
              + '<span class="fs-1 fw-bold me-1 ms-4">%S</span> Sec'));
          });

          

      });*/
      $(window).scroll(function() {
        if ($(this).scrollTop()>2500)
         {
            $('.big-btn,.bottom-fade').hide(10000);
         }
        else
         {
          $('.big-btn,.bottom-fade').show(10000);
         }
     });
     
     //$('#cardnumber').mask('0000 0000 0000 0000');
     //$('#expiration').mask('00/00');
     
    /* $('form input').on("invalid", function(event) {
      $(this).setCustomValidity('Please Enter valid email')
     });
     
     $('form input').on("input", function(event) {
      $(this).setCustomValidity('')
     });*/
  } );



  function submitpath(formid, path) {
    var tmpaction = $('#' + formid).attr('action');
    $('#' + formid).attr('action', path);
    $('#' + formid).submit();
    $('#' + formid).attr('action', tmpaction);
  }

  function loadimage(f, imgelem) {
    var file = document.getElementById(f).files[0];
    //var file = file.files[0];
    var reader  = new FileReader();
    // it's onload event and you forgot (parameters)
    reader.onload = function(e)  {
        var image = document.getElementById(imgelem);
        // the result image data
        image.src = e.target.result;
     }
     // you have to declare the file loading
     reader.readAsDataURL(file);
  }

  function profile_photo(id, im) {
    var file = document.getElementById(id).files[0];
    var reader  = new FileReader();
    // it's onload event and you forgot (parameters)
    reader.onload = function(e)  {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            $('#' + im ).attr('img', '/' + this.responseText);
          }
        };
        xhttp.open("POST", server + "/profilephoto", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("photo=" + encodeURIComponent(e.target.result));
     }
     // you have to declare the file loading
     reader.readAsDataURL(file);
  }

  function upload_photos(id, t) {
    var file = document.getElementById(id).files[0];
    var reader  = new FileReader();
    // it's onload event and you forgot (parameters)
    reader.onload = function(e)  {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            $('#uploadedphotos').append('<li style="position: relative;"><img src="' + server +'uploads/'+ this.responseText +'" class="img-responsive" onclick="popImage(this, \'' + this.responseText + '\')"><a href="#" onclick="deleteImage(this, \''+ this.responseText +'\')" style="position: absolute; right: 1em; top: 1em; color: red;" title="Delete"><i class="fa fa-trash" style="font-size: 30px;"></i>Delete</a></li>');
            $('#uploaded_files').val($('#uploaded_files').val() + this.responseText + ',');
          }
        };
        xhttp.open("POST", server + "/uploadphoto/" + t, true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("photo=" + encodeURIComponent(e.target.result));
     }
     // you have to declare the file loading
     reader.readAsDataURL(file);
  }

  function deleteImage(o, f) {
    $(o).parent().remove();
    $('#uploaded_files').val($('#uploaded_files').val().replace(f + ',', ''));
    $('#deleted_files').val($('#deleted_files').val() + f + ',');
  }

  function popcauseImage(o, f) {
    $('#permitmodal').modal('show');
    $('#modal-img').attr('src', $(o).attr('src'));
  }

  function popImage(o, f) {
    $('#photomodal').modal('show');
    $('#photomodal-img').attr('src', $(o).attr('src'));
  }

  function validate_coupon(url) {
    var gh_discount_count = $('#gh_discount_count').val();
    if(gh_discount_count <= 0) {
      $.ajax({
        url: url + '?code=' + $('#coupon_code').val(),
        dataType: "json",
        success: function(data) {
          if(data.message == 'Coupon applied successfully') {
            $('#promotioncode_status').html('Promocode has been applied');
            $('#promo_id').val(data.id);
            $('#promotioncode_status').css('color','#00FF00');
            $('#freeentrydonations').append('<div>Promo Code <span class=" float-end d-inline-block"><small><i class="fa fa-dollar"></i></small> <strong>0.00</strong></span></div><h5 class="mt-2">Promocode '+ $('#coupon_code').val() +' applied</h5>');
          }
          else {
            $('#promotioncode_status').html('Invalid code');
            $('#promotioncode_status').css('color','#FF0000');
          }
          $('#entrytotal').html(data.total);
          $('#gh_discount_count').val(gh_discount_count+1);
        }
      });
    }
  }

  function validate_promocode(url) {
    var gh_discount_count = $('#gh_discount_count').val();
    if(gh_discount_count <= 0) {
      $.ajax({
        url: url + '?code=' + $('#coupon_code').val(),
        dataType: "json",
        success: function(data) {
          if(data.message == 'Coupon applied successfully') {
            $('#promotioncode_status').html('Promocode has been applied');
            $('#promo_id').val(data.id);
            $('#promotioncode_status').css('color','#00FF00');
            $('#checkoutcartitems').append('<tr><td class="p-1">' + data.result + '</td><td class="align-middle text-nowrap"><small><i class="fa fa-dollar"></i></small> <strong>0.00</strong></td></tr>');
          }
          else {
            $('#promotioncode_status').html('Invalid code');
            $('#promotioncode_status').css('color','#FF0000');
          }
          $('#entrytotal').html(data.total);
          $('#gh_discount_count').val(gh_discount_count+1);
        }
      });
    }
  }

  function add_charity(obj, url, id) {
    $.ajax({
        url: url + '?id='+id,
        success: function(data) {
            $('#freeentrydonations').append('<div>Donation <span class=" float-end d-inline-block"><small><i class="fa fa-dollar"></i></small> <strong>2.00</strong></span></div> <h5 class="mt-2">Entry with Donation of $2</h5>');
            $('#entrytotal').html(data.grandtotal);
        }
    });
  }

  function selectattr(obj, at, v) {
    $('#attr'+at).val(v);
    $('.causeattr' + at).removeClass('selected-attr');
    $(obj).addClass('selected-attr');
    //$(obj).css('backgroundColor', '#0033ff');
  }

  function addtoCart(id='') {
    //$('#sajong_ecom_add_cart_form').ajaxSubmit({
    $.ajax({
      type:"post",
      url: server + '/add/cart', 
      data: $('#sajong_ecom_add_cart_form'+id).serialize(),
      success: function(res) {// Need to change it to serialize
        $('#cartadded-popup').modal('show');
        $('#addcartpopup_productprices').html($('#productprices').html());
        $('#header_cartcount').html(res.cartcount);
        $('#header_popup_cartcount').html(res.cartcount);
        li = '';
        for(i = 0; i < res.cartitems.length; i++) {
          li += '<div class="row fw-normal border-bottom pb-2 mb-2"><div class="col-8 dropcarttext">'+ res.cartitems[i].title + ' '+ res.cartitems[i].color + ' '+ res.cartitems[i].size +'</div><div class="col-4 text-end"><span class="pdtlstcash fw-bold">'+ res.cartitems[i].total +'</span></div></div>';
        }
          
        $('#header_popup_cartcontents').html(li);
        $('#ecomheader_carttotal').html(res.ordertotal);
        $('#ecomheader_cartbutton').show();
        $('#header_cartcount').show();
        $('#cartdrop').addClass('show');
        $('#header_cart_summary').addClass('show');
      },
      error: function() {
        $('#ecom-addtocart-overlay').hide();
        alert('We are facing some technical issue. Please try again.');
      }
    });
    return false;
  }

  function validateCart() {
    $('#ecom-addtocart-overlay').show();
    $('#sajong_ecom_add_cart_form').ajaxSubmit({
      type:"post",
     // url: url, 
      data: $('#sajong_ecom_add_cart_form').serialize(),
      success: function(res) {// Need to change it to serialize
        $('#carterror').hide();
        $('#ecom-addtocart-overlay').hide();
        $('#cartadded-popup').modal('show');
        $('#header_cartcount').html(res.cartcount);
        $('#header_popup_cartcount').html(res.cartcount);
        li = '';
        for(i = 0; i < res.cartitems.length; i++) {
          li += '<div class="row fw-normal border-bottom pb-2 mb-2"><div class="col-8 dropcarttext">'+ res.cartitems[i].title + ' '+ res.cartitems[i].color + ' '+ res.cartitems[i].size +'</div><div class="col-4 text-end"><span class="pdtlstcash fw-bold">'+ res.cartitems[i].total +'</span></div></div>';
        }
          
        $('#header_popup_cartcontents').html(li);
        $('#ecomheader_carttotal').html(res.ordertotal);
        $('#ecomheader_cartbutton').show();
        $('#header_cartcount').show();
        $('#cartdrop').addClass('show');
        $('#header_cart_summary').addClass('show');
      },
      error: function() {
        $('#ecom-addtocart-overlay').hide();
        alert('We are facing some technical issue. Please try again.');
      }
    });
    return false;
  }


      
  function getsize(url, obj, cid, pid) {
    $('.product-colour').addClass('active');
    $(obj).removeClass('active');
    $('#product_color').val(cid);
    $('#product_size').val('');
    $('#product_id').val(pid);
    $.ajax({
      type: "POST",
      dataType: "json",
      url: url,
      data: { cid: cid, pid:pid },
      success: function(response) {//designmainimage
        $('#product_id').val(response.sizes[0].vid);
        $('#product_size').val(response.sizes[0].id);
        $('#productprices').html('<small>$</small>' + (response.sizes[0].price/100));
        var s = '<h3>Size</h3>';
        for(i in response.sizes) {
          if(i==0) {
            s += '<div class="form-check form-check-inline mt-3 me-4"><input class="form-check-input" type="radio" id="sizebox{{key}}" name="sizebox" value="{{ psz.id }}" checked onclick="getprice(this, \'' + url.replace('size', 'price') +'\', ' + response.sizes[i].id + ', ' + response.sizes[i].vid + '); "><label class="form-check-label ms-2" for="sizebox'+ i +'">' + response.sizes[i].name + '</label></div>';
          }
          else {
            s += '<div class="form-check form-check-inline mt-3 me-4"><input class="form-check-input" type="radio" id="sizebox{{key}}" name="sizebox" value="{{ psz.id }}" onclick="getprice(this, \'' + url.replace('size', 'price') +'\', ' + response.sizes[i].id + ', ' + response.sizes[i].vid + '); "><label class="form-check-label ms-2" for="sizebox'+ i +'">' + response.sizes[i].name + '</label></div>';
          }
        }
        $('#productsizes').html(s);
        var prodimgs = response.images;
        $('#ua_prod_mainimage').attr('src', '/' + prodimgs[0].image);
        $('#item-added-cart-img').attr('src', '/' + prodimgs[0].image);
        var sliderimg = '';
        var sliderbtn = '';
        for(i in prodimgs) {
          if(i == 0) {
            sliderbtn += '<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="' + i + '" class="active" aria-current="true" aria-label="Slide 1"></button>';
            sliderimg += '<div class="carousel-item active"> <img src="' + prodimgs[i].image + '" class="d-block w-100" alt="' + response.sizes[0].title + '"> </div>';
          }
          else {
            sliderbtn += '<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="' + i + '" aria-current="true" aria-label="Slide 1"></button>';
            sliderimg += '<div class="carousel-item"> <img src="' + prodimgs[i].image + '" class="d-block w-100" alt="' + response.sizes[0].title + '"> </div>';
          }
        }
        $('#product_indicator_buttons').html(sliderbtn);
        $('#product_variation_images').html(sliderimg);
        $('#product_variation_price').html('' + (response.sizes[0].price/100));
        $('#product_id').val(response.sizes[0].vid);
      }
    });
  }
      
  function getprice(obj, url, fid, vid) {
    $('#product_size').val(fid);
    $('#product_id').val(vid);
    $.ajax({
      type: "POST",
      url: url,
      dataType: "json",
      data: { fid: fid, vid:vid },
      success: function(response) {
        $('#product_variation_price').html('' + (response.price/100));
      }
    });
  }
  
  $(document).ready(function(){
    $('#register-form').validate({
      rules: {
        'firstname': {
            required: true,
        },
        'lastname': {
          required: true,
        },
        'email': {
          required: true,
          email:true,
        },
        'phone': {
          required: true,
        },
        'password': {
          required: true,
          minlength: 5
        },
        'cpassword': {
          required: true,
          equalTo: "#password"
        }
      },
      messages: {
        'firstname': {
          required: "First Name is required",
        },
        'lastname': {
          required: "Last Name is required",
        },
        'email': {
          required: 'Email is required',
          email:'Please check the Email format',
        },
        'phone': {
          required: 'Phone is required',
        },
        'password': {
          required: 'Password is required',
          minlength: 'Min Password length is 5'
        },
        'cpassword': {
          required: 'Confirm Password is required',
          equalTo: 'Passwords does not match'
          
        }
      }
    });
	});