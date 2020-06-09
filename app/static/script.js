$(document).ready(function () {
  $('.dropdown-menu a').click(function () {
    $('#selected').text($(this).text());
  });

  $("#inputGroupFile01").change(function () {
    let fileName = $(this).val().split('\\').pop();
    fileName = fileName.length <= 16 ? fileName : fileName.substr(0, 16) + "...";
    $(this).next('.custom-file-label').addClass("selected").html(fileName);
    const fileExtensions = ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'pdf', 'txt']
    if (fileExtensions.includes($(this).val().substr($(this).val().lastIndexOf('.') + 1).toLowerCase())) {
      $("#error").hide()
      $('input[type="submit"]').addClass('bg-primary').removeClass('btn-disabled').removeClass('bg-dark');
      $('input[type="submit"]').prop('disabled', false);
    } else {
      $("#error").show().text("Format Invalid (Acceptable formats: jpg/jpeg, png, gif, bmp, pdf, txt)")
      $('input[type="submit"]').addClass('btn-disabled').addClass('bg-dark').removeClass('bg-primary');
      $('input[type="submit"]').prop('disabled', true)
    }
  })

  $("#target").submit(function (event) {
    event.preventDefault();
    $("#overlay").css("display", "flex")
    const file = $('#inputGroupFile01')[0].files[0];
    const language = $('#inputGroupSelect01').val();
    const formData = new FormData()

    formData.append('file', file);
    formData.append('language', language)

    fetch('/', {
      method: 'POST',
      body: formData
    })
      .then(response => {
        if (response.status === 200)
          return response.blob();
        else
          return response.json()
      })
      .then(blob => {
        if (blob.error) {
          $("#error").show().text(blob.error)
          $("#overlay").hide()
        } else {
          $("#error").hide()
          const url = window.URL.createObjectURL(blob);
          // const a = document.createElement('a');
          // a.href = url;
          // a.text = "filename.mp3";
          // $("#player").append(a);
          // window.audio = new Audio();
          // window.audio.src = url;
          // window.audio.play();  
          $("#aud").attr('src', url).attr('type', 'audio/mpeg')
          $("#overlay").hide()
        }
      })
      .catch(error => console.log(error))
  })
})