<!DOCTYPE html>
<html lang=ja>
  <head>
    <meta charset="UTF-8">
    <title>タイトルページ</title>
  </head>

  <body>
    <h1>タイトルページ</h1>
    <h2>URL入力</h2>
    <form method="GET" action="/check_result">
    <!--<input type="text" name="url" placeholder="https://www.yahoo.co.jp">-->
    <input type="text" name="url" value="https://www.yahoo.co.jp">
    <input type="text" name="tag" placeholder="取得したいタグを入力">
    <input type="text" name="word" placeholder="取得したいワードを入力">
    <input type="submit" value="送信する">
    </form>
  </body>

</html>
