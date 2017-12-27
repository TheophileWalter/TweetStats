/* TweetStats
 *
 * Fichier       ./front/classes/json-explorer.js
 * Description   Classe pour le dessin d'un explorateur de JSON, étend HtmlDisplay
 * Auteurs       Théophile Walter
 */

class JsonExplorer extends HtmlDisplay {

    /*
     * Constructeur de la classe JsonExplorer
     * 
     * @params
     *   element: l'élément DOM à utiliser comme parent ("div" de préférence)
     */
    constructor(element) {
        // Appel du constructeur parent
        super(element);
    }

    /*
     * Dessine l'explorateur de JSON en HTML
     * 
     * @params
     *   data: Un objet JSON à afficher
     */
    draw(data) {

        // Appel de la méthode mère
        super.draw(data);

        // Appel la méthode récursive qui va dessiner le JSON
        this._draw(data, this.element);
        
    }

    /*
     * Méthode récursive de dessin d'un sous-élement JSON dans un élement DOM donné
     * 
     * @params
     *   data: Un sous-objet JSON à afficher
     *   el:   L'élément DOM à afficher
     */
    _draw(data, el) {
        for (var key in data) {
            console.log(key);
        }
    } 

}