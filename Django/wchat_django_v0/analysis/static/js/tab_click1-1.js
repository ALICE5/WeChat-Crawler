$(document).ready(function(){
				$("#tab_a1").click(function(){
					$("#tab_l1").addClass("active");
					$("#tab_l2").removeClass();
					$("#tab_l3").removeClass();
					$("#tab_l4").removeClass();
			    		$("#box_chart1").show();
			    		$("#box_chart2").hide();
			    		$("#box_chart3").hide();
			    		$("#box_chart4").hide();                  			    		
			  	});
			  	
			  	$("#tab_a2").click(function(){
			  		$("#tab_l1").removeClass();
					$("#tab_l2").addClass("active");
					$("#tab_l3").removeClass();
					$("#tab_l4").removeClass();
			    		$("#box_chart1").hide();
			    		$("#box_chart2").show();
			    		$("#box_chart3").hide();
			    		$("#box_chart4").hide();
			    		var myChart = echarts.init(document.getElementById('box_chart2'));
			    		var option = {
					    title : {
					        text: '双数值轴折线',
					        subtext: '纯属虚构'
					    },
					    tooltip : {
					        trigger: 'axis',
					        axisPointer:{
					            show: true,
					            type : 'cross',
					            lineStyle: {
					                type : 'dashed',
					                width : 1
					            }
					        },
					        formatter : function (params) {
					            return params.seriesName + ' : [ '
					                   + params.value[0] + ', ' 
					                   + params.value[1] + ' ]';
					        }
					    },
					    legend: {
					        data:['数据1','数据2']
					    },
					    toolbox: {
					        show : true,
					        feature : {
					            mark : {show: true},
					            dataZoom : {show: true},
					            dataView : {show: true, readOnly: false},
					            magicType : {show: true, type: ['line', 'bar']},
					            restore : {show: true},
					            saveAsImage : {show: true}
					        }
					    },
					    calculable : true,
					    xAxis : [
					        {
					            type: 'value'
					        }
					    ],
					    yAxis : [
					        {
					            type: 'value',
					            axisLine: {
					                lineStyle: {
					                    color: '#dc143c'
					                }
					            }
					        }
					    ],
					    series : [
					        {
					            name:'数据1',
					            type:'line',
					            data:[
					                [1.5, 10], [5, 7], [8, 8], [12, 6], [11, 12], [16, 9], [14, 6], [17, 4], [19, 9]
					            ],
					            markPoint : {
					                data : [
					                    // 纵轴，默认
					                    {type : 'max', name: '最大值',symbol: 'emptyCircle', itemStyle:{normal:{color:'#dc143c',label:{position:'top'}}}},
					                    {type : 'min', name: '最小值',symbol: 'emptyCircle', itemStyle:{normal:{color:'#dc143c',label:{position:'bottom'}}}},
					                    // 横轴
					                    {type : 'max', name: '最大值', valueIndex: 0, symbol: 'emptyCircle', itemStyle:{normal:{color:'#1e90ff',label:{position:'right'}}}},
					                    {type : 'min', name: '最小值', valueIndex: 0, symbol: 'emptyCircle', itemStyle:{normal:{color:'#1e90ff',label:{position:'left'}}}}
					                ]
					            },
					            markLine : {
					                data : [
					                    // 纵轴，默认
					                    {type : 'max', name: '最大值', itemStyle:{normal:{color:'#dc143c'}}},
					                    {type : 'min', name: '最小值', itemStyle:{normal:{color:'#dc143c'}}},
					                    {type : 'average', name : '平均值', itemStyle:{normal:{color:'#dc143c'}}},
					                    // 横轴
					                    {type : 'max', name: '最大值', valueIndex: 0, itemStyle:{normal:{color:'#1e90ff'}}},
					                    {type : 'min', name: '最小值', valueIndex: 0, itemStyle:{normal:{color:'#1e90ff'}}},
					                    {type : 'average', name : '平均值', valueIndex: 0, itemStyle:{normal:{color:'#1e90ff'}}}
					                ]
					            }
					        },
					        {
					            name:'数据2',
					            type:'line',
					            data:[
					                [1, 2], [2, 3], [4, 2], [7, 5], [11, 2], [18, 3]
					            ]
					        }
					    ]
					};
                    myChart.setOption(option);
			  	});
			  	
			  	$("#tab_a3").click(function(){
			  		$("#tab_l1").removeClass();
					$("#tab_l2").removeClass();
					$("#tab_l3").addClass("active");
					$("#tab_l4").removeClass();
					$("#box_chart1").hide();
			    		$("#box_chart2").hide();
			    		$("#box_chart3").show();
			    		$("#box_chart4").hide();
			    		var myChart = echarts.init(document.getElementById('box_chart3'));
			    		var option = {
					    title : {
					        text: '某地区蒸发量和降水量',
					        subtext: '纯属虚构'
					    },
					    tooltip : {
					        trigger: 'axis'
					    },
					    legend: {
					        data:['蒸发量','降水量']
					    },
					    toolbox: {
					        show : true,
					        feature : {
					            mark : {show: true},
					            dataView : {show: true, readOnly: false},
					            magicType : {show: true, type: ['line', 'bar']},
					            restore : {show: true},
					            saveAsImage : {show: true}
					        }
					    },
					    calculable : true,
					    xAxis : [
					        {
					            type : 'category',
					            data : ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
					        }
					    ],
					    yAxis : [
					        {
					            type : 'value'
					        }
					    ],
					    series : [
					        {
					            name:'蒸发量',
					            type:'bar',
					            data:[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
					            markPoint : {
					                data : [
					                    {type : 'max', name: '最大值'},
					                    {type : 'min', name: '最小值'}
					                ]
					            },
					            markLine : {
					                data : [
					                    {type : 'average', name: '平均值'}
					                ]
					            }
					        },
					        {
					            name:'降水量',
					            type:'bar',
					            data:[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
					            markPoint : {
					                data : [
					                    {name : '年最高', value : 182.2, xAxis: 7, yAxis: 183, symbolSize:18},
					                    {name : '年最低', value : 2.3, xAxis: 11, yAxis: 3}
					                ]
					            },
					            markLine : {
					                data : [
					                    {type : 'average', name : '平均值'}
					                ]
					            }
					        }
					    ]
					};
                    
			    		myChart.setOption(option);
			  	});
			  	
			  	$("#tab_a4").click(function(){
			  		$("#tab_l1").removeClass();
					$("#tab_l2").removeClass();
					$("#tab_l3").removeClass();
					$("#tab_l4").addClass("active");
			    		$("#box_chart1").hide();
			    		$("#box_chart2").hide();
			    		$("#box_chart3").hide();
			    		$("#box_chart4").show();
					var myChart = echarts.init(document.getElementById('box_chart4'));
					var option = {
					    tooltip : {
					        trigger: 'axis'
					    },
					    legend: {
					        data:['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']
					    },
					    toolbox: {
					        show : true,
					        feature : {
					            mark : {show: true},
					            dataView : {show: true, readOnly: false},
					            magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
					            restore : {show: true},
					            saveAsImage : {show: true}
					        }
					    },
					    calculable : true,
					    xAxis : [
					        {
					            type : 'category',
					            boundaryGap : false,
					            data : ['周一','周二','周三','周四','周五','周六','周日']
					        }
					    ],
					    yAxis : [
					        {
					            type : 'value'
					        }
					    ],
					    series : [
					        {
					            name:'邮件营销',
					            type:'line',
					            stack: '总量',
					            itemStyle: {normal: {areaStyle: {type: 'default'}}},
					            data:[120, 132, 101, 134, 90, 230, 210]
					        },
					        {
					            name:'联盟广告',
					            type:'line',
					            stack: '总量',
					            itemStyle: {normal: {areaStyle: {type: 'default'}}},
					            data:[220, 182, 191, 234, 290, 330, 310]
					        },
					        {
					            name:'视频广告',
					            type:'line',
					            stack: '总量',
					            itemStyle: {normal: {areaStyle: {type: 'default'}}},
					            data:[150, 232, 201, 154, 190, 330, 410]
					        },
					        {
					            name:'直接访问',
					            type:'line',
					            stack: '总量',
					            itemStyle: {normal: {areaStyle: {type: 'default'}}},
					            data:[320, 332, 301, 334, 390, 330, 320]
					        },
					        {
					            name:'搜索引擎',
					            type:'line',
					            stack: '总量',
					            itemStyle: {normal: {areaStyle: {type: 'default'}}},
					            data:[820, 932, 901, 934, 1290, 1330, 1320]
					        }
					    ]
					};
					myChart.setOption(option);
			
			    		
			  	});
		});