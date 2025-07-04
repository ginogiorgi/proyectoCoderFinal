document.addEventListener("DOMContentLoaded", function () {
    // Evitar doble declaración de variables y listeners
    if (window._sidebarMenuInit) return;
    window._sidebarMenuInit = true;

    let arrow = document.querySelectorAll(".arrow");
    for (var i = 0; i < arrow.length; i++) {
        arrow[i].addEventListener("click", (e) => {
            let arrowParent = e.target.parentElement.parentElement; //selecting main parent of arrow
            arrowParent.classList.toggle("showMenu");
        });
    }
    let sidebar = document.querySelector(".sidebar");
    let sidebarBtn = document.getElementById("sidebar-toggle");
    // Eliminar cualquier interacción del ícono hamburguesa
});

// Si usás datepicker, asegurate de que jQuery esté cargado antes de este script.
// Si no usás datepicker, puedes eliminar este bloque para evitar el error de $ no definido.
// $('.datepicker').datepicker({
//     weekdaysShort: ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'],
//     showMonthsShort: true
//   });
