$(document).ready(function(){
  // Toggle between light and dark modes
  $('button.mode-switch').click(function(){
    $('body').toggleClass('dark');
  });
  
  // Close the right-side panel
  $(".btn-close-right").click(function () {
    $(".right-side").removeClass("show");
    $(".expand-btn").addClass("show");
  });
  
  // Expand the right-side panel
  $(".expand-btn").click(function () {
    $(".right-side").addClass("show");
    $(this).removeClass("show");
  });
});
