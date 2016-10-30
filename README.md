# How to contribute

Repo này gồm 2 branch chính:

* master: chứa generated html, **KHÔNG** push thứ gì vào branch này.
* develop: đây là branch chính để làm việc. checkout sang đây để thực hiện các
thay đổi. Xem tiếp dưới đây

## Các bước để publish nội dung

* Checkout repo sang branch `develop`: `git checkout develop`.
* Tiến hành thực hiện thay đổi
* Sau khi thay đổi xong thì `git add` rồi `git commit` như bình thường.
* Push thay đổi lên branch `develop`
* Generate code HTML: `make html`. Các file sẽ được gen vào folder `output`
* Cài tool `ghp-import` bằng `pip install ghp-import`
* Import các generated files vào branch master: `ghp-import -b master output/`.
  Có thể đọc thêm về tool `ghp-import` để có các option mở rộng khác.
* Push branch `master` lên để publish nội dung: `git push origin master`
