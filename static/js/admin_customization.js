// admin_customization.js

function hideColumn(columnIndex) {
    const table = document.querySelector('.result_list');
    console.log(table)
    const rows = table.querySelectorAll('tr');
    console.log(rows)
    rows.forEach((row) => {
      const cells = row.cells;
      if (cells.length > columnIndex) {
        cells[columnIndex].style.display = 'none';
      }
    });
  
    // Store the column preference in a cookie
    document.cookie = `hiddenColumn=${columnIndex}; path=/`;
  }
  
  function showHiddenColumns() {
    const hiddenColumn = getCookieValue('hiddenColumn');
    if (hiddenColumn) {
      const table = document.querySelector('.result_list');
      const rows = table.querySelectorAll('tr');
  
      rows.forEach((row) => {
        const cells = row.cells;
        if (cells.length > hiddenColumn) {
          cells[hiddenColumn].style.display = '';
        }
      });
    }
  }
  
  function getCookieValue(name) {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(`${name}=`)) {
        return cookie.substring(name.length + 1);
      }
    }
    return '';
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    showHiddenColumns();
  
    const buttons = document.querySelectorAll('.hide-column-button');
    buttons.forEach((button, index) => {
      button.addEventListener('click', () => {
        hideColumn(index);
      });
    });
  });
  