# StarWays 

>El site generado se ha creado usando el framework [Hugo](https://gohugo.io/) y con la ayuda de una de sus plantillas [Hugo Themes Showcase](https://themes.gohugo.io/).

Esta página web muestra los ficheros markdown que Hugo ha generado en forma de HTML.

La plantilla de Hugo trae incorporado tanto HTML como scss, que es una extensión de css.

Hemos editado el fichero 'toml' para cambiar los datos de la plantilla, además de editar el scss añadiendo, entre otras cosas, las _medias querys_.


# Using

1. [Install Hugo](https://gohugo.io/overview/installing/)
2. Clone this repository
```bash
git clone https://github.com/gohugoio/hugoBasicExample.git
cd hugoBasicExample
```
3. Clone the repository you want to test. If you want to test all Hugo Themes then follow the instructions provided [here](https://github.com/gohugoio/hugoThemes#installing-all-themes)
4. Run Hugo and select the theme of your choosing
```bash
hugo server -t YOURTHEME
```
5. Under `/content/` this repository contains the following:
- A section called `/post/` with sample markdown content
- A headless bundle called `homepage` that you may want to use for single page applications. You can find instructions about headless bundles over [here](https://gohugo.io/content-management/page-bundles/#headless-bundle)
- An `about.md` that is intended to provide the `/about/` page for a theme demo
6. If you intend to build a theme that does not fit in the content structure provided in this repository, then you are still more than welcome to submit it for review at the [Hugo Themes](https://github.com/gohugoio/hugoThemes/issues) respository
