import { useState } from "react";
import { Link } from "react-router-dom";
import API from "../services/api";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const login = async () => {
    if (!username || !password) {
      alert("Please enter username and password");
      return;
    }

    try {
      setLoading(true);

      const res = await API.post("/login", {
        username,
        password,
      });

      localStorage.setItem(
        "token",
        res.data.access_token
      );

      window.location.href = "/dashboard";

    } catch (error) {
      alert(
        error.response?.data?.detail ||
        "Login Failed"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Login</h1>

      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) =>
          setUsername(e.target.value)
        }
      />

      <br />
      <br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <br />
      <br />

      <button
        onClick={login}
        disabled={loading}
      >
        {loading ? "Logging in..." : "Login"}
      </button>

      <p>
        Don't have an account?{" "}
        <Link to="/register">
          Register
        </Link>
      </p>
    </div>
  );
}

export default Login;