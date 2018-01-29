<!DOCTYPE html>
<html lang=ja>
  <head>
    <meta charset="UTF-8">
    <title>タイトルページ</title>
  </head>

  <body>
    <h1>タイトルページ</h1>
    <h2>URL入力</h2>
    <form method="GET" action="/check">
    <input type="text" name="url"></p>
    <input type="submit" value="送信する">
    </form>

    <h2>結果出力のページ</h2>
    <p>{{data}}<p>
    <a href="/">return to HOME</a>
    </p>

  </body>

</html>
