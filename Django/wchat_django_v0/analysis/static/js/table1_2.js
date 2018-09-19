$("#table1").bootstrapTable({ // 对应table标签的id
			url: "/static/json/page1_2_table.json", // 获取表格数据的url
			cache: false, // 设置为 false 禁用 AJAX 数据缓存， 默认为true
			striped: true, //表格显示条纹，默认为false
			pagination: true, // 在表格底部显示分页组件，默认false
			pageList: [10, 20], // 设置页面可以显示的数据条数
			pageSize: 10, // 页面数据条数
			pageNumber: 1, // 首页页码
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

