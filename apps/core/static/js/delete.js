(function (){
    const btnElimacion=document.querySelectorAll(".btnEliminacion");

    btnElimacion.forEach(btn=>{
    btn.addEventListener('click',(e)=>{
        const confirmacion=confirm('seguro que quiere elimnar el curso?');
        if(!confirmacion){
            e.preventDefault();
        }
    });
});
})();