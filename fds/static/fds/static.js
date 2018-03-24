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

function getData(){

  // overall_rank_chart
  var overall_rank_data = document.getElementsByName('main_ranks');
  var main_ctx = document.getElementById('overall_rank_canvas').getContext('2d');
  var overall_rank_chart = new Chart(main_ctx, {
    type:'pie',
    data:{
      labels:["Excellent", "Good", "Average", "Worst"],
      datasets:[{
        data: [overall_rank_data[0].value, overall_rank_data[1].value, overall_rank_data[2].value, overall_rank_data[3].value],
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

  // Question1_rank_chart
  var question1_rank_data = document.getElementsByName('question1_rank');
  var question1_ctx = document.getElementById('question1_rank_canvas').getContext('2d');
  var question1_rank_chart = new Chart(question1_ctx, {
    type:'pie',
    data:{
      labels:["Excellent", "Good", "Average", "Worst"],
      datasets:[{
        data: [question1_rank_data[0].value, question1_rank_data[1].value, question1_rank_data[2].value, question1_rank_data[3].value],
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


  // Question2_rank_chart
  var question2_rank_data = document.getElementsByName('question2_rank');
  var question2_ctx = document.getElementById('question2_rank_canvas').getContext('2d');
  var question2_rank_chart = new Chart(question2_ctx, {
    type:'pie',
    data:{
      labels:["Excellent", "Good", "Average", "Worst"],
      datasets:[{
        data: [question2_rank_data[0].value, question2_rank_data[1].value, question2_rank_data[2].value, question2_rank_data[3].value],
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

  var question3_rank_data = document.getElementsByName('question3_rank');
  var question3_ctx = document.getElementById('question3_rank_canvas').getContext('2d');
  var question3_rank_chart = new Chart(question3_ctx, {
    type:'pie',
    data:{
      labels:["Excellent", "Good", "Average", "Worst"],
      datasets:[{
        data: [question3_rank_data[0].value, question3_rank_data[1].value, question3_rank_data[2].value, question3_rank_data[3].value],
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
