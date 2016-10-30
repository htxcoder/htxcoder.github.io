# How to contribute

Repo này gồm 2 branch chính:

* master: chứa generated html, **KHÔNG** push thứ gì vào branch này.
* develop: đây là branch chính để làm việc. checkout sang đây để thực hiện các
thay đổi. Xem tiếp dưới đây

## Các bước để publish

* checkout repo sang branch `develop`: `git checkout develop`.
* Tiến hành thực hiện thay đổi
* Sau khi thay đổi xong thì `git add` rồi `git commit`.
* Push lên branch `develop`
* Generate code HTML: `make html`. Các file được gen vào folder `output`
* Cài tool `ghp-import` bằng `pip install ghp-import`
* Import các generated files vào branch master: `ghp-import -b master output/`
* Push branch `master` lên: `git push origin master`
