/* TweetStats
 *
 * Fichier       ./front/classes/util.js
 * Description   Contient des fonctions utiles
 * Auteurs       Théophile Walter
 */

var util = {

    /*
     * Prépare une chaîne de caractères à être affichée en HTML
     * 
     * @params
     *   text: Le texte à préparer
     * 
     * @return
     *   Le texte préparé avec les caractères spéciaux HTML échappés
     */
    escapeHtml: function(text) {
        if (typeof text != "string") {
            return text;
        }
        var map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    },

    /*
     * Décode une chaîne de caractères HTML
     * 
     * @params
     *   text: Le texte à décoder
     * 
     * @return
     *   Le texte décodé avec les caractères spéciaux HTML transformés
     */
    decodeHtml: function(text) {
        if (typeof text != "string") {
            return text;
        }
        var map = {
            '&amp;'  : '&',
            '&lt;'   : '<',
            '&gt;'   : '>',
            '&quot;' : '"',
            '&#039;' : "'"
        };
        return text.replace(/&amp;|&lt;|&gt;|&quot;|&#039;/g, function(m) { return map[m]; });
    },

    /*
     * Récupère le contenu d'un cookie
     * 
     * @params
     *   cname: Le nom du cookie
     * 
     * @return
     *   La valeur du cookie
     *   undefined si le cookie n'existe pas
     * 
     * @notes
     *   Source : https://www.w3schools.com/js/js_cookies.asp
     */
    getCookie: function(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for(var i = 0; i <ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return undefined;
    },

    /*
     * Défini la valeur d'un cookie
     * 
     * @params
     *   cname:  Le nom du cookie
     *   cvalue: La valeur du cookie
     *   exdays: La durée de vie (en jours) du cookie
     * 
     * @notes
     *   Source : https://www.w3schools.com/js/js_cookies.asp
     */
    setCookie: function(cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays*24*60*60*1000));
        var expires = "expires="+ d.toUTCString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    } 
    
};