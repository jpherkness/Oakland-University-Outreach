# HTML

### What is HTML ?

HTML stands for **hypertext markup language**. It's a standard markup language for web pages created in 1990 by physicist
Tim Berners-Lee.

### Creating your workspace

Let's quickly create a place to put all of our projects.

Create a folder named `Website Workspace` on your desktop

### Our First Website

Open up Brackets or Notepad, and type the following code

```html
<html>
    Hello World!
</html>
```
### Saving Our First Website

Save the file within your `Website Workspace` folder, and call it <br> `hello-world.html`

### Viewing Our First Website

Right click on your *hello-world.html* file | *Open With* | *Chrome*

### Tags & Elements

Tags act like containers, telling you information about what lies between its _opening_ and _closing_ tags.

```html
<p>This is only the beginning</p>
```

^ Tags and elements are generally used interchangably

^ All tags should be lowercase

---

### Here is a very basic html document.

```html
<!DOCTYPE html>
<html>

  <head>
  	<title>This is the title</title>
  </head>

  <body>
    Hello World!
  </body>

</html>
```

> The DOCTYPE tag describes the filetype.
<br>
The html element wraps the entire webpage.
<br>
The head element contains information about the webpage.
<br>
The title element, which goes inside the head element, contains the title of the webpage.
<br>
The body element contains the content of the webpage.

---

# Element *Attributes*

Attributes give us information about the element they belong to

## *name* = "*value*"

<br />

```html
<h1 species="human">Joshua</h1>
```

^ In the example, `species` represents the name of the attribute, and `"human"` represents the value

^ We can relate these to atributes that a person has: Hair color, Birthplace, Eye color, height, etc..

---

### *Tearing* apart
### a web page

---

# *Tearing* apart a web page

You can look at how a web page is created by *right clicking anywhere* on the page | *Inspect element*

<br>

Go to any website, and take a look at how it's made

^You can also right click anywhere on the page | *View source*

---

###*Text* & Formatting

---

### |------------------- _**Heading Elements**_ -------------------|

# *`<h1></h1>` ... `<h6></h6>`*

```html
<h1>Level 1 heading</h1>
<h2>Level 2 heading</h2>
<h3>Level 3 heading</h3>
<h4>Level 4 heading</h4>
<h5>Level 5 heading</h5>
<h6>Level 6 heading</h6>
```

^`<h1>`
^`<h2>`
^`<h3>`
^`<h4>`
^`<h5>`
^`<h6>`

---

### |-- _**Paragraph Element**_ --|

# *`<p></p>`*

<br>

```html
<p>I'm a paragraph.</p>
<p>Same     here.</p>
```

---

### |------------- _**Link Element**_ -------------|

# *`<a href=""></a>`*


<br>

```html
<a href="http://wwwp.oakland.edu">Oakland University</a>
```

<br>

^ A link has an address to a specific and defined *href* attribute

^`href` stands for hyperlink reference

---

# *"Quotes"*

> "The true sign of intelligence is not knowledge but imagination"
	- Albert Einstein

You can describe a short quote using the *`<q>`* element

You can describe a long quote using the *`<blockquote>`* element

```html
<!-- Short/Inline Quote -->
<q>Nothing endures but change</q>

<!-- Block Quote -->
<blockquote>
	<p>To be, or not to be, that is the question</p>
	<footer>- Shakespeare</footer>
</blockquote>
```

---

# *Formatting*

```html
<b>Bold</b>
<strong>Strong</strong>

<i>Italic</i>
<em>Emphisis</em>

<small>Small</small>
<mark>Marked/Highlighted</mark>
<del>Deleted</del>
<ins>Inserted</ins>
<sub>Subscript</sub>
<sup>Superscript</sup>
```

---

# *Pre Formatting*

Pre formatted text is described using the *`<pre>`* tag

<br>

```html
<pre>
Text in a pre element
is displayed in a fixed-width
font, and it preserves
both      spaces and
line break
</pre>
```

---

# *Commenting*

Comments are a necessary part of computer science. They will not be rendered by your web browser.

<br>

```html
<!-- This is my name -->
<p>Joshua Herkness</p>
```

---

###*Images*

---

### |-- _**Image Element**_ --|

# *`<img>`*

The image element does *not* have a closing tag

![](http://www2.shutterstock.com/blog/wp-content/uploads/sites/5/2015/01/img263.jpg)

<br>

```html
<img src="flower.jpg" alt="Flower" width="100" height="100">
```
<br>

^ The source file (*src*), alternative text (*alt*), and size (*width* and *height*) are provided as attributes

^ The source (src) of an image is expected to be in the same folder as the webpage, unless specified otherwise

---

### *Unordered* and
### *Ordered* lists

---

# *Unordered* list

<br>

```html
<!-- Unordered list -->
<ul>
	<!-- List Item -->
	<li>Bacon</li>
	<li>Eggs</li>
	<li>Waffles!</li>
</ul>
```

---

# *Ordered* list

<br>

```html
<!-- Ordered list -->
<ol>
	<!-- List Item -->
	<li>Bacon</li>
	<li>Eggs</li>
	<li>Waffles!</li>
</ol>
```

---

#[fit] Create your
#[fit] *website*

---

# Create your *website*

Put all of the following on your website

- Name
- Short description
- Favorite quote
- Top three favorite films, in order
- Some of your favorite foods
- Favorite song + Link (_**Youtube**_)
- Favorite ice cream + Image
