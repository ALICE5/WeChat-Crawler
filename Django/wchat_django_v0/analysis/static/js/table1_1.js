$("#table").bootstrapTable({ // 对应table标签的id
			url: "/static/json/page1_1_table.json", // 获取表格数据的url
			cache: false, // 设置为 false 禁用 AJAX 数据缓存， 默认为true
			striped: true, //表格显示条纹，默认为false
			pagination: true, // 在表格底部显示分页组件，默认false
			pageList: [10, 20], // 设置页面可以显示的数据条数
			pageSize: 10, // 页面数据条数
			pageNumber: 1, // 首页页码
//			sidePagination: 'server', // 设置为服务器端分页
//			queryParams: function(params) { // 请求服务器数据时发送的参数，可以在这里添加额外的查询参数，返回false则终止请求
//	
//				return {
//					pageSize: params.limit, // 每页要显示的数据条数
//					offset: params.offset, // 每页显示数据的开始行号
//					sort: params.sort, // 要排序的字段
//					sortOrder: params.order, // 排序规则
//					dataId: $("#dataId").val() // 额外添加的参数
//				}
//			},
//			sortName: 'id', // 要排序的字段
//			sortOrder: 'desc', // 排序规则
			columns: [
//				{
//					checkbox: true, // 显示一个勾选框
//					align: 'center' // 居中显示
//				}, 
			{
				field: 'time', // 返回json数据中的name
				title: '时间', // 表格表头显示文字
				align: 'center', // 左右居中
				valign: 'middle' // 上下居中
			}, {
				field: 'view_num', 
				title: '浏览量PV', 
				align: 'center', 
				valign: 'middle' 
			}, {
				field: 'like_num', 
				title: '点赞数', 
				align: 'center', 
				valign: 'middle' 
			}, {
				field: 'comment_num',
				title: '评论数',
				align: 'center',
				valign: 'middle'
			}, {
				field: 'count',
				title: '发文数',
				align: 'center',
				valign: 'middle'
			}, {
				field: 'view_mean',
				title: '平均浏览量',
				align: 'center',
				valign: 'middle'
			}, {
				field: 'like_mean',
				title: '平均点赞数',
				align: 'center',
				valign: 'middle'
			}],
			onLoadSuccess: function() { //加载成功时执行
				console.info("加载成功");
			},
			onLoadError: function() { //加载失败时执行
				console.info("加载数据失败");
			}
		})