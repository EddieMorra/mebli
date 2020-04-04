$(document).ready(function(){

    
  $( ".slider_nav" ).each(function() {
    q = $(".slick-track").length;
    console.log(q + ' ffhfhfh');
    if (q.length == 1) {
      $(this).hide();
    }
  });

///////////////////////////////////////////////////
  // $( ".tot" ).each(function() {
  //   dol_kurs = $(this).html();
  //   total = $('.kursd').html();
  //   q = dol_kurs * total
  //   $('.tot').html(q.toFixed(0) + ' UAH');
  // });
  
  // $( ".prrrice" ).each(function() {
  //   total = $(this).html();
  //   dol_kurs = $('.kursd').html();

  //   q = dol_kurs * total

  //   console.log(q + ' llllllll');

  //   $(this).html(q.toFixed(0) + ' UAH');
  // });

  // $( ".total_f" ).each(function() {
  //   total = $(this).html();
  //   dol_kurs = $('.kursd').html();

  //   q = dol_kurs * total

  //   console.log(q + ' llllllll');

  //   $(this).html(q.toFixed(0) + ' UAH');
  // });
  ////////////////////////////////////////////////////
  // $( ".kursd" ).each(function() {
  //   dol_kurs = $(this).html();
  //   total = $('.tot').html();
  //   q = dol_kurs * total
  //   $('.tot').html(q.toFixed(0) + ' UAH');
  // });
  // $( ".price_wrapper" ).each(function() {
  //   i = $(this).find('.price').html();
  //   sum = i * 30.0
  //   // console.log(i);
  //   $(this).find('.price_uah').html(sum.toFixed(0));
  // });

    
    if (window.location.pathname !== '/') {
      $('.top_item').hide();
    };

    $( ".listpage:not(:has(div))" ).each(function() {
        $(this).siblings('.empty_text').addClass('empty');
    });
    // $( ".product_r_wrapper" ).each(function() {
    //     $(this).find('label').html('Кількість:');
    // });
    // $( ".cardd" ).each(function() {
    //     getContentHeight = $(this).outerHeight();
    //     console.log("zzzz" + getContentHeight);
    //     $( ".cardd" ).css('height', getContentHeight);
    // });


    
    // $('.q option').addClass('zzzz')
    $( ".q" ).each(function()  {
        // console.log('aaazzzz');
        

        // setTimeout(function(){
        //     console.log();
        //   }, 2000);
        var option = document.querySelector('#id_quantity');
        option.onchange=function(){
            // $('.subm').trigger('click');
            // console.log(this.value);
            $(this).siblings().trigger('click');
        };
     
    });

    $( ".oform" ).click(function()  {
      // var option = document.querySelector('#id_quantity');
      $(".subm").trigger('click');
    });



    $(".butn").click(function(){
      $(".input").addClass("active").focus;
      $(this).addClass("animate");
      // $(".input").val("");
    });

 
    $(".mob_mtn").click(function(){
      $(this).toggleClass("active");
        var q = $(".mob_mtn");
      if (q.hasClass("active")) {
        $(".mob_menu").addClass('open');
      } else {
        $(".mob_menu").removeClass('open');
      }
    });

    $(".close_btn").click(function(){
      $('.mob_menu').removeClass("open"),
      $('.mob_mtn').removeClass("active");
    });


    $(window).scroll(function() {
      if ($(this).scrollTop() > 400) {
          if ($('#upbutton').is(':hidden')) {
              $('#upbutton').css({opacity : 1}).fadeIn('slow');
          }
      } else { $('#upbutton').stop(true, false).fadeOut('fast'); }
  });
  $('#upbutton').click(function() {
      $('html, body').stop().animate({scrollTop : 0}, 300);
  });


    $('.first_slider').slick({
        infinite: true,
        // centerMode: true,
        // centerPadding: '50px',
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        pauseOnHover: false,
        autoplaySpeed: 5000,
        speed: 1000,
        dots: true,
        // cssEase: 'linear',
        draggable: true,
        prevArrow: '<i class="fa fa-angle-left"></i>',
        nextArrow: '<i class="fa fa-angle-right"></i>'
    });

    $('.new_product_sl').slick({
        infinite: true,
        pauseOnHover: false,
        centerMode: true,
        centerPadding: '60px',
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        speed: 900,
        cssEase: 'linear',
        draggable: true,
        prevArrow: '<i class="fa fa-angle-left"></i>',
        nextArrow: '<i class="fa fa-angle-right"></i>',
        adaptiveHeight: false,
        responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
               
              }
            },
            {
              breakpoint: 992,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
          ]
    });



    $('.slider_for').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      infinite: true,

      // centerMode: true,
      // centerPadding: '0px',
      
      autoplay: false,
      pauseOnHover: false,
      autoplaySpeed: 5000,
      speed: 500,
      fade: true,

      asNavFor: '.slider_nav',
      adaptiveHeight: true,
    });

    $('.slider_nav').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      // centerPadding: '15px',
      asNavFor: '.slider_for',
    
      infinite: true,
     
      centerMode: true,
      focusOnSelect: true,
      prevArrow: '<i class="fa fa-angle-left"></i>',
      nextArrow: '<i class="fa fa-angle-right"></i>',
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
           
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
     
      ]
    });



});


