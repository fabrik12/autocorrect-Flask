function showTab(tabId) {
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));

    const activeTab = document.getElementById(tabId);
    activeTab.classList.add('active');

    const inputType = document.getElementById('input_type');
    if (tabId === 'textTab') {
        inputType.value = 'text';
    } else if (tabId === 'fileTab') {
        inputType.value = 'file';
    }
}

showTab('textTab');

function toggleHighlighting() {
    // Obtener el checkbox
    var checkbox = document.getElementById("toggleHighlight");
    // Seleccionar todos los elementos con la clase 'corrected-word'
    var elementos = document.querySelectorAll(".corrected-word");
    
    // Si el checkbox está marcado, añadir la clase que aplica negrita; si no, la removemos
    elementos.forEach(function(el) {
        if (checkbox.checked) {
            el.style.fontWeight = "bold";
        } else {
            el.style.fontWeight = "normal"; 
        }
    });
}
