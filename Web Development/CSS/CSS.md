# [fit] CSS

---

### What is *CSS* ?

---

### *CSS* OR *CASCADING STYLE SHEET* IS A STYLE SHEET LANGUAGE USED FOR DESCRIBING THE *LOOK AND FORMATTING* OF A DOCUMENT WRITTEN IN A MARKUP LANGUAGE.

---

# A *CSS RULE SET* CONSISTS OF A *SELECTOR* AND A *DECLARATION BLOCK*

```CSS
/* p is a Selector */
/* color:blue is a Declaration */

p{
	color:blue;
}
```

---

### *SELECTORS* SPECIFY WHICH *ELEMENTS* <br> THE RULE APPLIES TO

---

# *TYPE SELECTORS*

You can use any HTML tag as a selector.

```CSS
h1, h2, h3 { 

}

p{

}

q{

}
```

---

### *DECLARATIONS* SPECIFY HOW THESE *ELEMENTS* SHOULD *APPEAR*

---

# *DECLARATIONS*

Here are a few examples of various declarations you can use.

```css
color: blue;
background-color: #aaaaaa
background-image:url(image.png);
padding: 10px;
margin: 5px;
width: 100%
font-style: italic;
font-weight: bold;
```

---

# USING *INTERNAL CSS*

CSS can be embeded into an HTML file by including the following code
inside your head element.

```html
<head>
    <style type="text/css">
		p{
			color: #e76324;
		}
    </style>
</head>
```

---

# USING *EXTERNAL CSS*

The *<link>* element can be used in an HTML document to tell the
browser where to find the CSS file.

It should be placed inside the head element.

```html
<link href="css/styles.css" type="text/css" rel="stylesheet" />
```