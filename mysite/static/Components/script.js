$(document).ready(function () {
  
  // Navbar: Cargar la navbar
  function loadNavbar() {
    $('#navbar-placeholder').load('../Components/navbar.html', function(response, status, xhr) {
      if (status == "error") {
        console.error("Error al cargar la navbar: " + xhr.status + " " + xhr.statusText);
      }
    });
  }

  // Footer: Cargar el footer
  function loadFooter() {
    $('#footer-placeholder').load('../Components/footer.html', function(response, status, xhr) {
      if (status == "error") {
        console.error("Error al cargar el footer: " + xhr.status + " " + xhr.statusText);
      }
    });
  }

  // Cargar componentes de navbar y footer
  loadNavbar();
  loadFooter();

  // Formulario de Reservación: Validar y enviar el formulario
  $('#reservationForm').submit(function(event) {
    event.preventDefault();
    var name = $('#name').val();
    var email = $('#email').val();
    var phone = $('#phone').val();
    var date = $('#date').val();
    var time = $('#time').val();

    // Validar el nombre para que contenga solo letras
  var nameRegex = /^[a-zA-Z\s]+$/;
  if (!nameRegex.test(name)) {
      alert('Por favor, introduce un nombre válido (solo letras).');
      return false;
  }

  // Validar el formato del teléfono (+569XXXXXXXX)
  var phoneRegex = /^\+569\d{8}$/;
  if (!phoneRegex.test(phone)) {
      alert('Por favor, introduce un número de teléfono válido (+569XXXXXXXX).');
      return false;
  }

  // Validar que la fecha no sea anterior a la actual
  var today = new Date();
  var selectedDate = new Date(date);
  if (selectedDate < today) {
      alert('Por favor, selecciona una fecha futura.');
      return false;
  }
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, introduce un correo electrónico válido.');
        return false;
    }

     // Validar que la hora esté entre 12 y 19 horas (de mediodía a las 7 PM)
    var selectedTime = new Date('1970-01-01T' + time + ':00');
    var startTime = new Date('1970-01-01T12:00:00');
    var endTime = new Date('1970-01-01T19:00:00');
    if (selectedTime < startTime || selectedTime > endTime) {
        alert('Por favor, selecciona una hora entre las 12:00 PM y las 7:00 PM.');
        return false;
    }

    
    if (name.trim() === '' || email.trim() === '' || phone.trim() === '' || date.trim() === '' || time.trim() === '') {
        alert('Por favor, completa todos los campos.');
        return false;
    }


    alert('Formulario enviado con éxito.');
  });

  // Mostrar modal al cargar la página
  $('#myModal').modal('show');

  // Promociones: Cargar imágenes aleatorias de comida
  function cargarImagenesAleatorias() {
    $.get("https://www.themealdb.com/api/json/v1/1/random.php", function(data) {
        var meal = data.meals[0];
        if (meal) {
            $("#promocion .card-img").eq(0).attr("src", meal.strMealThumb);
        } else {
            $("#promocion .card-text").html("Error al cargar la comida.");
        }
    });

    $.get("https://www.themealdb.com/api/json/v1/1/random.php", function(data) {
        var meal = data.meals[0];
        if (meal) {
            $("#promocion .card-img").eq(1).attr("src", meal.strMealThumb);
        } else {
            $("#promocion .card-text").html("Error al cargar la comida.");
        }
    });

    $.get("https://www.themealdb.com/api/json/v1/1/random.php", function(data) {
        var meal = data.meals[0];
        if (meal) {
            $("#promocion .card-img").eq(2).attr("src", meal.strMealThumb);
        } else {
            $("#promocion .card-text").html("Error al cargar la comida.");
        }
    });

    $(".card").each(function(index) {
        var tarjeta = $(this);
        $.get("https://www.themealdb.com/api/json/v1/1/random.php", function(data) {
            var meal = data.meals[0];
            if (meal) {
                tarjeta.find(".card-img-top").attr("src", meal.strMealThumb);       
            } else {
                tarjeta.find(".card-text").html("Error al cargar la comida.");
            }
        });
    });
  }

  // Llamar a la función para cargar las imágenes aleatorias
  cargarImagenesAleatorias();

  // Categorías de Comida: Paginación y manejo de clics
  var currentPage = 1;
  var categoriesPerPage = 5; // Número de categorías por página
  var categories = []; // Array para almacenar las categorías

  // Función para mostrar categorías según la página actual
  function showCategories(page) {
    $('.categoria').hide();
    for (var i = (page - 1) * categoriesPerPage; i < page * categoriesPerPage; i++) {
        $('.categoria').eq(i).show();
    }
  }

  // Manejar clic en los enlaces de paginación
  $('.pagination a').on('click', function (e) {
    e.preventDefault();  
    var page = parseInt($(this).attr('data-page'));
    if (!isNaN(page)) {
      currentPage = page;
      showCategories(currentPage);
    }
  });

  // Mostrar categorías al inicio
  showCategories(currentPage);

  // Manejar clic en el botón "Previous"
  $('#previousPage').on('click', function () {
    if (currentPage > 1) {
      currentPage--;
      showCategories(currentPage);
    }
  });

  // Manejar clic en el botón "Next"
  $('#nextPage').on('click', function () {
    if (currentPage < $('.page-item').length - 2) {
      currentPage++;
      showCategories(currentPage);
    }
  });

  // Petición GET a la API para obtener las categorías de comida
  $.get("https://www.themealdb.com/api/json/v1/1/categories.php", function (data) {
    categories = data.categories;
    $.each(categories, function (i, item) {
      $("#categorias").append(
        '<div class="col-md-5 mb-4 categoria" style="display:none;">' +
        '<div class="card" style="background-color:#FCD1A0 ;">' +
        '<img src="' + item.strCategoryThumb + '" class="card-img-top" alt="...">' +
        '<div class="card-body">' +
        '<h5 class="card-title">' + item.strCategory + '</h5>' +
        '<div class="descripcion-categoria" style="display:none;">' + item.strCategoryDescription + '</div>' +
        '<br>' +
        '<a href="#" class="btn btn-primary btn-ver-mas" style="background-color:#E74C3C ;">Ver más</a>' +
        '</div>' +
        '</div>' +
        '</div>'
      );
    });

    showCategories(currentPage);
  });

  // Función para manejar el clic en el botón "Ver más"
  $(document).on('click', '.btn-ver-mas', function (e) {
    e.preventDefault();
    var descripcion = $(this).closest('.card').find('.descripcion-categoria');
    descripcion.toggle();
  });
});

