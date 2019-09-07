const slider = document.querySelector('.slider');

const classEditing = function (edit, element, elementClass) {
    element = document.querySelector(element);
    if (edit === 'add') {
        element.classList.add(elementClass);
    } else if (edit === 'remove') {
        element.classList.remove(elementClass);
    } else {
        console.log(`Please enter add/remove instead of ${edit}`);
    }
};

function CreateArticle(header, summeryText, link) {
    this.header = header;
    this.summeryText = summeryText;
    this.link = link;
    this.articleWrapper = document.createElement("div");

    this.add = function (element) {
        //Header html creation
        let header = document.createElement("h2");
        let link = document.createElement("a");
        let headerNode = document.createTextNode(this.header);

        link.href = this.link;
        link.target = '_blank';

        link.append(headerNode);
        header.append(link);
        header.classList.add('article-title');

        this.articleWrapper.append(header);


        //Summery Text html creation
        let summeryText = document.createElement("p");
        let summeryTextNode = document.createTextNode(this.summeryText);

        summeryText.append(summeryTextNode);
        summeryText.classList.add('summery-text');

        this.articleWrapper.append(summeryText);
        this.articleWrapper.classList.add('article-wrapper');

        element.appendChild(this.articleWrapper)
    };

    this.remove = function () {
        this.articleWrapper.remove()
    }
}

let articleArray = [];

const getArticles = function () {

    const siteName = document.querySelector('.select-blog').value;

    fetch(`https://blog-scrapper.appspot.com/get-articles/${siteName}`).then((data) =>
        data.json().then(function (articles) {
            //Clears the html off the page if you are selecting a new
            if (articleArray.length !== 0) {
                articleArray.forEach(function (article) {
                    article.remove();
                });
                articleArray = [];
            }

            articles.forEach(function (article) {
                articleArray.push(
                    new CreateArticle(
                        article.header,
                        article.summeryText,
                        article.link,
                    ))
            });

            articleArray.forEach(function (article) {
                article.add(slider);
            })
        }));
};


getArticles('The-Crazy-Programmer');

