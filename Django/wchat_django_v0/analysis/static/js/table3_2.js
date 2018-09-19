$("#table1").bootstrapTable({ // 对应table标签的id
	url: "/static/json/page3-2-readNum.json", // 获取表格数据的url
	cache: false, // 设置为 false 禁用 AJAX 数据缓存， 默认为true
	striped: true, //表格显示条纹，默认为false
	columns: [
	{
		field: 'id', // 返回json数据中的name
		title: '排名', // 表格表头显示文字
		align: 'center', // 左右居中
		valign: 'middle' // 上下居中
	}, {
		field: 'title',
		title: '文章名',
		align: 'center',
		valign: 'middle'
	}, {
		field: 'readNum',
		title: '阅读数',
		align: 'center',
		valign: 'middle'
	}, {
		field: 'date',
		title: '发文时间',
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

$("#table2").bootstrapTable({ // 对应table标签的id
	url: "/static/json/page3-2-likenum.json", // 获取表格数据的url
	cache: false, // 设置为 false 禁用 AJAX 数据缓存， 默认为true
	striped: true, //表格显示条纹，默认为false
	columns: [
	{
		field: 'id', // 返回json数据中的name
		title: '排名', // 表格表头显示文字
		align: 'center', // 左右居中
		valign: 'middle' // 上下居中
	}, {
		field: 'title',
		title: '文章名',
		align: 'center',
		valign: 'middle'
	}, {
		field: 'likeNum',
		title: '点赞数',
		align: 'center',
		valign: 'middle'
	}, {
		field: 'date',
		title: '发文时间',
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

$("#table3").bootstrapTable({ // 对应table标签的id
	url: "/static/json/page3-2-comment.json", // 获取表格数据的url
	cache: false, // 设置为 false 禁用 AJAX 数据缓存， 默认为true
	striped: true, //表格显示条纹，默认为false
	columns: [
	{
		field: 'id', // 返回json数据中的name
		title: '排名', // 表格表头显示文字
		align: 'center', // 左右居中
		valign: 'middle' // 上下居中
	}, {
		field: 'title',
		title: '文章名',
		align: 'center',
		valign: 'middle'
	}, {
		field: 'commentNum',
		title: '评论数',
		align: 'center',
		valign: 'middle'
	}, {
		field: 'date',
		title: '发文时间',
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