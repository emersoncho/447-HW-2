import React from 'react'

function ArticleList(props) {
    const editArticle = (article) => {
        props.editArticle(article)
    }
    return (
        <div>
            {props.article && props.articles.map(article => {
        return (
          <div key = {article.id}>
            <h2>{article.name}</h2>
            <p>{article.points}</p>

            <div className = "row">
                <div className = "col-md-1">
                    <button className = "btn btn-primary">Update</button>
                    onClick = {() => editArticle(article)}
                </div> 
                <div className = "col-md-1">
                    <button className = "btn btn-danger">Delete</button>
                    onClick = {() => deleteArticle(article)}
                </div> 
                </hr>
          </div>
        )
      })}
        </div>
    )

}

export default ArticleList