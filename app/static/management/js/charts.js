
$(document).ready(function() {

    function initLineChart(id, month=false) {
        /* ----------==========     Daily Sales Chart initialization    ==========---------- */
        let chartData = $(id);
        if (chartData.length > 0) {
            let values = chartData.data()['update']
            let labels;

            if (month) {
                labels = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
            } else {
                labels = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
            }

            dataDailySalesChart = {
                labels: labels,
                series: [
                    values
                ]
            };
    
            optionsDailySalesChart = {
                lineSmooth: Chartist.Interpolation.cardinal({
                    tension: 0
                }),
                low: 0,
                high: Math.max(values) + (Math.max(values) - Math.min(values))/10, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
                chartPadding: {
                    top: 10,
                    right: 0,
                    bottom: 0,
                    left: 0
                },
            }
    
            var dailySalesChart = new Chartist.Line(id, dataDailySalesChart, optionsDailySalesChart);
    
            md.startAnimationForLineChart(dailySalesChart);
        } 
    }


    
    initLineChart('#websiteViewsChart', month=true);
    initLineChart('#dailySalesChart');
    initLineChart('#completedTasksChart');

    $(window).resize(function() {
        md.initSidebarsCheck();
      
        // reset the seq for charts drawing animations
        seq = seq2 = 0;
      
        setTimeout(function() {
            initLineChart('#dailySalesChart');
            initLineChart('#completedTasksChart');
            initLineChart('#websiteViewsChart');
        }, 500);
      });
})