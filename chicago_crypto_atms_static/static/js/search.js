/**
 * Chicago Crypto ATMs - Search Functionality
 * This script handles client-side search for the static site deployment
 */

document.addEventListener('DOMContentLoaded', function() {
  // Get the search form
  const searchForm = document.getElementById('search-form');
  let atmData = null;
  
  // Load the ATM data for advanced search capabilities
  fetch('/static/js/data.json')
    .then(response => response.json())
    .then(data => {
      atmData = data;
      console.log('ATM data loaded successfully');
    })
    .catch(error => {
      console.error('Error loading ATM data:', error);
    });
  
  if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const searchQuery = document.getElementById('search-input').value.toLowerCase().trim();
      
      // Redirect to the appropriate page based on search
      if (searchQuery.includes('bitcoin') || searchQuery === 'btc') {
        window.location.href = '/cryptocurrency/bitcoin.html';
      } else if (searchQuery.includes('ethereum') || searchQuery === 'eth') {
        window.location.href = '/cryptocurrency/ethereum.html';
      } else if (searchQuery.includes('xrp') || searchQuery === 'ripple') {
        window.location.href = '/cryptocurrency/xrp.html';
      } else if (searchQuery.includes('tether') || searchQuery === 'usdt') {
        window.location.href = '/cryptocurrency/tether.html';
      } else if (searchQuery.includes('usdc')) {
        window.location.href = '/cryptocurrency/usdc.html';
      } else if (searchQuery.includes('dogecoin') || searchQuery === 'doge') {
        window.location.href = '/cryptocurrency/dogecoin.html';
      } else if (searchQuery.includes('litecoin') || searchQuery === 'ltc') {
        window.location.href = '/cryptocurrency/litecoin.html';
      } else if (searchQuery.includes('shiba') || searchQuery === 'shib') {
        window.location.href = '/cryptocurrency/shiba-inu.html';
      } else if (searchQuery.includes('dai')) {
        window.location.href = '/cryptocurrency/dai.html';
      } else if (searchQuery.includes('bitcoin cash') || searchQuery === 'bch') {
        window.location.href = '/cryptocurrency/bitcoin-cash.html';
      } else if (searchQuery.includes('loop')) {
        window.location.href = '/neighborhood/loop.html';
      } else if (searchQuery.includes('river north')) {
        window.location.href = '/neighborhood/river-north.html';
      } else if (searchQuery.includes('lincoln park')) {
        window.location.href = '/neighborhood/lincoln-park.html';
      } else if (searchQuery.includes('wicker park')) {
        window.location.href = '/neighborhood/wicker-park.html';
      } else if (searchQuery.includes('logan square')) {
        window.location.href = '/neighborhood/logan-square.html';
      } else if (searchQuery.includes('west loop')) {
        window.location.href = '/neighborhood/west-loop.html';
      } else if (searchQuery.includes('south loop')) {
        window.location.href = '/neighborhood/south-loop.html';
      } else if (searchQuery.includes('gold coast')) {
        window.location.href = '/neighborhood/gold-coast.html';
      } else if (searchQuery.includes('lakeview')) {
        window.location.href = '/neighborhood/lakeview.html';
      } else if (searchQuery.includes('uptown')) {
        window.location.href = '/neighborhood/uptown.html';
      } else if (atmData) {
        // Search for ATMs by name, address, or other criteria
        const results = searchAtms(searchQuery, atmData.atms);
        if (results.length > 0) {
          // If we have a specific ATM match, go to its neighborhood
          window.location.href = '/neighborhood/' + results[0].neighborhood + '.html';
        } else {
          // If no match, show a message
          alert('No results found for: ' + searchQuery + '. Please try another search term.');
        }
      } else {
        // If ATM data not loaded or no match, show a message
        alert('No results found for: ' + searchQuery + '. Please try another search term.');
      }
    });
  }
  
  /**
   * Search ATMs by name, address, or other criteria
   * @param {string} query - The search query
   * @param {Array} atms - The array of ATMs to search
   * @return {Array} - The filtered array of ATMs
   */
  function searchAtms(query, atms) {
    if (!query || !atms) return [];
    
    return atms.filter(atm => {
      return (
        atm.name.toLowerCase().includes(query) ||
        atm.address.toLowerCase().includes(query) ||
        atm.neighborhood.toLowerCase().includes(query) ||
        atm.cryptocurrencies.some(crypto => crypto.toLowerCase().includes(query))
      );
    });
  }
}); 