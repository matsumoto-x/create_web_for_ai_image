function previewFile(file) {
	console.debug("debug")
	// プレビュー画像を追加する要素
	const preview = document.getElementById('preview');
	const prename = document.getElementById('prename');
	prename.remove()
	//preview.removeChild(preview.firstElementChild);
	// FileReaderオブジェクトを作成
	const reader = new FileReader();
  
	// ファイルが読み込まれたときに実行する
	reader.onload = function (e) {
	  const imageUrl = e.target.result; // 画像のURLはevent.target.resultで呼び出せる

	  const img = document.createElement("img"); // img要素を作成
	  img.src = imageUrl; // 画像のURLをimg要素にセット
	  preview.appendChild(img); // #previewの中に追加
	}

	// いざファイルを読み込む
	reader.readAsDataURL(file);
  }
  
  // <input>でファイルが選択されたときの処理
  const fileInput = document.getElementById('id_image');
  const handleFileSelect = () => {
	const files = fileInput.files;
	for (let i = 0; i < files.length; i++) {
	  previewFile(files[i]);
	}
  }
  fileInput.addEventListener('change', handleFileSelect);