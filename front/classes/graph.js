/* TweetStats
 *
 * File          ./front/classes/graph.js
 * Description   Interface for Javascript classes wich draw some graphics
 * Authors       Théophile Walter
 */

class Graph {

    /*
     * Constructeur de la classe Graph
     * 
     * @params
     *   element: l'élément DOM canvas à utiliser pour le dessin
     *   context: le context 2D à utiliser pour le dessin
     */
    constructor(element, context) {
        this.element = element;
        this.context = context;
    }

    /*
     * Dessine le graphique en fonction des données entrées
     * 
     * @params
     *   data: les données à utiliser pour le dessin (le type dépend de la classe qui impélentera cette méthode)
     */
    draw(data) {
        // À implémenter dans les classes filles
    }

}