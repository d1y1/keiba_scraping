<!DOCTYPE html>
<html lang=ja>
<head>
  <meta charset="UTF-8">
  <title>タイトルページ</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">
  <link rel="stylesheet/less" type="text/css" href="style/style.less">
  <script src="//cdnjs.cloudflare.com/ajax/libs/less.js/2.7.2/less.min.js"></script>
</head>

<body>
<header>
  <h1>タイトルページ</h1>
</header>
<main>
  <h2>URL入力</h2>
  <span class="">
    <form method="GET" action="/check_result">
      <input type="text" name="url" value="https://www.yahoo.co.jp">
      <input type="text" name="tag" placeholder="取得したいタグを入力">
      <input type="text" name="word" placeholder="取得したいワードを入力">
      <input type="submit" value="送信する">
    </form>
  </span>
</main>
</body>

</html>
