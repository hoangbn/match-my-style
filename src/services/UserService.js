import axios from "axios";
const BACKEND_URL = "http://localhost:5000";
const USERS_URL = BACKEND_URL + "/users"

export default class UserService {
    /**
     * Create a new user
     * @param username of user
     */
    static async createUser(username) {
        await axios.post(USERS_URL, { username });
    }

    /**
     * Get user item links
     * @param username of user
     */
    static async getUserItems(username) {
        return await axios.get(USERS_URL + "/" + username);
    }

    /**
     * Add new pants to the user
     * @param username of user
     * @param type of item to add to the usr
     * @param imageFile of pants to upload and add as a link
     */
    static async addItem(username, type, imageFile) {
        const imageFormData = new FormData();
        imageFormData.append("file", imageFile);
        return (await axios.post(`${USERS_URL}/${username}/${type}`, imageFormData)).data;
    }

    /**
     * Add new pants to the user
     * @param username of user
     * @param imageFile of pants to upload and add as a link
     */
    static async addPants(username, imageFile) {
        return await UserService.addItem(username, "pants", imageFile);
    }

    /**
     * Add new shirt to the user
     * @param username of user
     * @param imageFile of shirt to upload and add as a link
     */
    static async addShirt(username, imageFile) {
        return await UserService.addItem(username, "shirts", imageFile);
    }
}
