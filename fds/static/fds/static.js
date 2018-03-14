function draw(){
  var ranks = document.getElementsByName('ranks');
  var ctx = document.getElementById('myCanvas').getContext('2d');
  var chart = new Chart(ctx, {
    type:'pie',
    data:{
      labels:["Excellent", "Good", "Average", "Worst"],
      datasets:[{
        data: [ranks[0].value, ranks[1].value, ranks[2].value, ranks[3].value],
        backgroundColor:[
          'rgba(75, 192, 192, 0.5)',
          'rgba(255, 206, 86, 0.5)',
          'rgba(255, 159, 64, 0.5)',
          'rgba(255, 99, 132, 0.5)'
        ],
        borderColor: [
          'rgba(75, 192, 192, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 99, 132, 1)'
        ],
        borderWidth: 2
      }]
    }
  });
}
