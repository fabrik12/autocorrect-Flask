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