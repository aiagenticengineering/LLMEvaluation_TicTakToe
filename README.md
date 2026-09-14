# 🤖 Two-LLM Tic-Tac-Toe

A Tic-Tac-Toe game powered by **two LLM-based players** using the **OpenAI Responses API and function/tool calling**.

Each LLM plays a different role:

* **Player X** — Aggressive strategist
* **Player O** — Defensive strategist

The LLMs don't directly manipulate the game board. Instead, they use tools exposed by the game engine to inspect the board, find available moves, make moves, and check the game status.

The project demonstrates how to build a simple **multi-agent LLM application with tool calling**.

---

## 🎯 Project Goal

The goal of this project is to demonstrate how two LLM agents can interact with a shared application state through tools.

Instead of asking an LLM to simply return a move, the LLM can interact with the game through functions such as:

```text
get_board()
get_available_moves()
make_move(position)
get_game_status()
```

The application remains responsible for enforcing the game rules.

### Core principle

> **LLMs make decisions. The game engine enforces the rules.**

---

## 🧠 Architecture

```text
                         ┌─────────────────────┐
                         │     Game Engine     │
                         │                     │
                         │  Board              │
                         │  Rules              │
                         │  Move Validation    │
                         │  Winner Detection   │
                         └──────────┬──────────┘
                                    │
                         Game Tools / Functions
                                    │
                ┌───────────────────┴───────────────────┐
                │                                       │
                ▼                                       ▼
       ┌─────────────────┐                     ┌─────────────────┐
       │     LLM X       │                     │     LLM O       │
       │                 │                     │                 │
       │ Aggressive      │                     │ Defensive       │
       │ Player          │                     │ Player          │
       └────────┬────────┘                     └────────┬────────┘
                │                                       │
                └──────────────────┬────────────────────┘
                                   │
                                   ▼
                            OpenAI Responses API
```

---

## 🔄 How the Game Works

The game follows this cycle:

```text
                    Start Game
                        │
                        ▼
                  Player X LLM
                        │
                        ▼
                 get_board()
                        │
                        ▼
             get_available_moves()
                        │
                        ▼
                LLM chooses move
                        │
                        ▼
                make_move(position)
                        │
                        ▼
                Validate the move
                        │
                        ▼
                Update the board
                        │
                        ▼
              get_game_status()
                        │
                  ┌─────┴─────┐
                  │           │
               Game Over    Continue
                              │
```
