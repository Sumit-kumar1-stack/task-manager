import { useState } from "react";
import { Link } from "react-router-dom";
import API from "../services/api";

function Register() {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);

  const register = async () => {
    if (
      !form.username ||
      !form.email ||
      !form.password
    ) {
      alert("Please fill all fields");
      return;
    }

    try {
      setLoading(true);

      await API.post(
        "/register",
        form
      );

      alert(
        "Registration Successful"
      );

      window.location.href = "/";

    } catch (error) {
      alert(
        error.response?.data?.detail ||
        "Registration Failed"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Register</h1>

      <input
        type="text"
        placeholder="Username"
        value={form.username}
        onChange={(e) =>
          setForm({
            ...form,
            username: e.target.value,
          })
        }
      />

      <br />
      <br />

      <input
        type="email"
        placeholder="Email"
        value={form.email}
        onChange={(e) =>
          setForm({
            ...form,
            email: e.target.value,
          })
        }
      />

      <br />
      <br />

      <input
        type="password"
        placeholder="Password"
        value={form.password}
        onChange={(e) =>
          setForm({
            ...form,
            password: e.target.value,
          })
        }
      />

      <br />
      <br />

      <button
        onClick={register}
        disabled={loading}
      >
        {loading
          ? "Registering..."
          : "Register"}
      </button>

      <p>
        Already have an account?{" "}
        <Link to="/">
          Login
        </Link>
      </p>
    </div>
  );
}

export default Register;